from PySide6.QtWidgets import (
    QWidget, QHBoxLayout, QVBoxLayout, QTableWidget, QTableWidgetItem,
    QHeaderView, QCheckBox, QLabel
)
from PySide6.QtCharts import QChart, QChartView, QPieSeries, QPieSlice, QBarSeries, QBarSet, QBarCategoryAxis, QValueAxis
from Componentes_Personalizado import Search_Bar, Button_Search
from PySide6.QtCore import Slot
from utils import variables
from controllers.tarea_controller import TareaController
from PySide6.QtGui import Qt, QFont, QPainter


class View_Tarea_Windows(QWidget):
    """
    Vista para la gestión de tareas de un usuario, con gráficos integrados en una estructura clara.
    """

    def __init__(self, parent=None):
        super().__init__(parent)

        # Layout principal
        self.resize(800, 900)
        self.layout_vertical_main = QVBoxLayout()
        self.setLayout(self.layout_vertical_main)

        # Layout horizontal para barra de búsqueda
        self.layout_horizontal_search_bar = QHBoxLayout()
        self.button_search = Button_Search(icon=variables.iconSearch, text="Buscar")
        self.search_bar = Search_Bar()

        # Tabla de tareas
        self.tabla_tarea = QTableWidget()
        self.tabla_tarea.setColumnCount(4)
        self.tabla_tarea.setHorizontalHeaderLabels(["Nombre", "Descripción", "Estado", "Activa"])

        self.header = self.tabla_tarea.horizontalHeader()
        self.header.setSectionResizeMode(QHeaderView.Stretch)

        # Añadir componentes al layout horizontal
        self.layout_horizontal_search_bar.addWidget(self.search_bar)
        self.layout_horizontal_search_bar.addWidget(self.button_search)

        # Añadir layout horizontal y tabla al layout principal
        self.layout_vertical_main.addLayout(self.layout_horizontal_search_bar)
        self.layout_vertical_main.addWidget(self.tabla_tarea)

        # Layout para los gráficos de pastel
        self.layout_horizontal_charts = QHBoxLayout()
        self.chart_estado = QChartView()
        self.chart_estado.setRenderHint(QPainter.Antialiasing)
        self.chart_activa = QChartView()
        self.chart_activa.setRenderHint(QPainter.Antialiasing)
        self.layout_horizontal_charts.addWidget(self.chart_estado)
        self.layout_horizontal_charts.addWidget(self.chart_activa)

        # Añadir layout de gráficos de pastel al layout principal
        self.layout_vertical_main.addLayout(self.layout_horizontal_charts)

        # Gráfico de barras
        self.chart_bar = QChartView()
        self.chart_bar.setRenderHint(QPainter.Antialiasing)
        self.layout_vertical_main.addWidget(self.chart_bar)

        # Etiqueta de resumen
        self.label_resumen = QLabel()
        self.layout_vertical_main.addWidget(self.label_resumen)

        # Variables
        self.tareas_originales = []

        # Obtener datos iniciales
        self.obtenerDatos()

        # Conectar eventos
        self.search_bar.textEdited.connect(self.cambioEnTexto)
        self.button_search.signal_presionado.connect(self.cambioEnTexto)

    def llenar_tabla(self, datos):
        """
        Llenar la tabla con los datos proporcionados.
        """
        self.tabla_tarea.setRowCount(len(datos))

        for fila, datos_fila in enumerate(datos):
            for columna, dato in enumerate(datos_fila):
                if columna == 3:  # Columna "Activa"
                    checkbox = QCheckBox()
                    checkbox.setChecked(dato == "Sí")
                    checkbox.setEnabled(False)
                    self.tabla_tarea.setCellWidget(fila, columna, checkbox)
                else:
                    item = QTableWidgetItem(dato)
                    item.setTextAlignment(Qt.AlignCenter)

                    # Aplicar estilo tachado si el estado es "Finalizado"
                    if columna == 2 and dato == "Finalizado":
                        font = item.font()
                        font.setStrikeOut(True)
                        item.setFont(font)

                    self.tabla_tarea.setItem(fila, columna, item)

    @Slot()
    def obtenerDatos(self):
        """
        Obtener las tareas del usuario y llenar la tabla.
        """
        try:
            tareas = TareaController().obtener_tareas_por_usuario(variables.usuario)
            if not tareas:
                raise ValueError("No se encontraron tareas.")

            self.tareas_originales = tareas
            self.actualizar_tabla_y_graficos(tareas)
        except Exception as e:
            print(f"Error al obtener las tareas: {e}")

    @Slot()
    def cambioEnTexto(self):
        """
        Actualizar la tabla en base al texto ingresado en la barra de búsqueda.
        """
        texto = self.search_bar.text().lower()
        tareas_filtradas = [
            tarea for tarea in self.tareas_originales
            if texto in tarea.nombre.lower() or texto in tarea.descripcion.lower() or texto in tarea.estado.lower()
        ]
        self.actualizar_tabla_y_graficos(tareas_filtradas)

    def actualizar_tabla_y_graficos(self, tareas):
        """
        Actualizar la tabla y los gráficos en base a las tareas proporcionadas.
        """
        datos = [[tarea.nombre, tarea.descripcion, tarea.estado, "Sí" if not tarea.estado == "Finalizado" else "No"]
                 for tarea in tareas]
        self.llenar_tabla(datos)
        self.actualizar_graficos(tareas)
        self.mostrar_resumen(tareas)

    def actualizar_graficos(self, tareas):
        """
        Actualizar los gráficos de tareas por estado y activas/inactivas.
        """
        estados = {"Pendiente": 0, "En proceso": 0, "Finalizado": 0}
        activos = {"Activas": 0, "Inactivas": 0}

        for tarea in tareas:
            if tarea.estado in estados:
                estados[tarea.estado] += 1
            if tarea.estado != "Finalizado":
                activos["Activas"] += 1
            else:
                activos["Inactivas"] += 1

        # Gráfico de pastel: Tareas por estado
        self.actualizar_pie_chart(self.chart_estado, "Tareas por Estado", estados)

        # Gráfico de pastel: Tareas activas/inactivas
        self.actualizar_pie_chart(self.chart_activa, "Tareas Activas/Inactivas", activos)

        # Gráfico de barras: Resumen de tareas por estado
        self.actualizar_bar_chart(estados)

    def actualizar_pie_chart(self, chart_view, title, data):
        """
        Actualizar un gráfico de pastel.
        """
        series = QPieSeries()
        for key, value in data.items():
            series.append(key, value)

        chart = QChart()
        chart.addSeries(series)
        chart.setTitle(title)
        chart_view.setChart(chart)

    def actualizar_bar_chart(self, data):
        """
        Actualizar el gráfico de barras con datos de tareas.
        """
        series = QBarSeries()
        bar_set = QBarSet("Tareas")
        for value in data.values():
            bar_set.append(value)
        series.append(bar_set)

        chart = QChart()
        chart.addSeries(series)
        chart.setTitle("Resumen de Tareas por Estado")
        chart.setAnimationOptions(QChart.SeriesAnimations)

        categories = list(data.keys())
        axis_x = QBarCategoryAxis()
        axis_x.append(categories)
        chart.addAxis(axis_x, Qt.AlignBottom)
        series.attachAxis(axis_x)

        axis_y = QValueAxis()
        axis_y.setRange(0, max(data.values()) + 1)
        chart.addAxis(axis_y, Qt.AlignLeft)
        series.attachAxis(axis_y)

        self.chart_bar.setChart(chart)

    def mostrar_resumen(self, tareas):
        """
        Mostrar resumen de tareas totales, estados y activas/inactivas.
        """
        total_tareas = len(tareas)
        pendientes = sum(1 for tarea in tareas if tarea.estado == "Pendiente")
        en_proceso = sum(1 for tarea in tareas if tarea.estado == "En proceso")
        finalizadas = sum(1 for tarea in tareas if tarea.estado == "Finalizado")
        activas = total_tareas - finalizadas

        resumen = (f"Número de tareas: {total_tareas}. "
                   f"Pendientes: {pendientes}, En proceso: {en_proceso}, Finalizadas: {finalizadas}. "
                   f"Activas: {activas}, Inactivas: {finalizadas}.")
        self.label_resumen.setText(resumen)
