from PySide6.QtWidgets import (
    QWidget, QHBoxLayout, QVBoxLayout, QTableWidget, QTableWidgetItem,
    QHeaderView, QCheckBox, QLabel
)
from PySide6.QtCharts import QChart, QChartView, QPieSeries, QPieSlice
from PySide6.QtCore import Slot, Qt
from PySide6.QtGui import QPainter
from utils import variables
from controllers.tarea_controller import TareaController
from Componentes_Personalizado import Search_Bar, Button_Search


class View_Tarea_Windows(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Layout principal
        self.resize(900, 900)
        self.layout_vertical_main = QVBoxLayout()
        self.setLayout(self.layout_vertical_main)

        # Barra de búsqueda
        self.layout_horizontal_search_bar = QHBoxLayout()
        self.search_bar = Search_Bar()
        self.button_search = Button_Search(icon=variables.iconSearch, text="Buscar")
        self.layout_horizontal_search_bar.addWidget(self.search_bar)
        self.layout_horizontal_search_bar.addWidget(self.button_search)

        # Tabla de tareas
        self.tabla_tarea = QTableWidget()
        self.tabla_tarea.setColumnCount(4)
        self.tabla_tarea.setHorizontalHeaderLabels(["Nombre", "Descripción", "Estado", "Activa"])
        self.tabla_tarea.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # Gráficas
        self.layout_horizontal_charts = QHBoxLayout()

        # Gráfica 1
        self.chart_estado = QChartView()
        self.chart_estado.setRenderHint(QPainter.Antialiasing)
        self.layout_horizontal_charts.addWidget(self.chart_estado)

        # Gráfica 2
        self.chart_activa = QChartView()
        self.chart_activa.setRenderHint(QPainter.Antialiasing)
        self.layout_horizontal_charts.addWidget(self.chart_activa)

        # Añadir widgets al layout principal
        self.layout_vertical_main.addLayout(self.layout_horizontal_search_bar)
        self.layout_vertical_main.addWidget(self.tabla_tarea)
        self.layout_vertical_main.addLayout(self.layout_horizontal_charts)

        # Resumen de tareas
        self.label_resumen = QLabel("")
        self.layout_vertical_main.addWidget(self.label_resumen)

        # Conexiones
        self.search_bar.textEdited.connect(self.cambioEnTexto)
        self.button_search.signal_presionado.connect(self.cambioEnTexto)

        # Datos iniciales
        self.tareas_originales = []
        self.obtenerDatos()

    def llenar_tabla(self, datos):
        self.tabla_tarea.setRowCount(len(datos))
        for fila, datos_fila in enumerate(datos):
            for columna, dato in enumerate(datos_fila):
                if columna == 3:
                    checkbox = QCheckBox()
                    checkbox.setChecked(dato == "Sí")
                    checkbox.setEnabled(False)
                    self.tabla_tarea.setCellWidget(fila, columna, checkbox)
                else:
                    item = QTableWidgetItem(dato)
                    item.setTextAlignment(Qt.AlignCenter)
                    if columna == 2 and dato == "Finalizado":
                        font = item.font()
                        font.setStrikeOut(True)
                        item.setFont(font)
                    self.tabla_tarea.setItem(fila, columna, item)

    @Slot()
    def obtenerDatos(self):
        try:
            tareas = TareaController().obtener_tareas_por_usuario(variables.usuario)
            self.tareas_originales = tareas
            self.actualizar_tabla_y_graficos(tareas)
        except Exception as e:
            print(f"Error al obtener las tareas: {e}")

    @Slot()
    def cambioEnTexto(self):
        texto = self.search_bar.text().lower()
        tareas_filtradas = [
            tarea for tarea in self.tareas_originales
            if texto in tarea.nombre.lower() or texto in tarea.descripcion.lower() or texto in tarea.estado.lower()
        ]
        self.actualizar_tabla_y_graficos(tareas_filtradas)

    def actualizar_tabla_y_graficos(self, tareas):
        datos = [
            [tarea.nombre, tarea.descripcion, tarea.estado, "Sí" if not tarea.estado == "Finalizado" else "No"]
            for tarea in tareas
        ]
        self.llenar_tabla(datos)
        self.actualizar_graficos(tareas)
        self.actualizar_resumen(tareas)

    def actualizar_graficos(self, tareas):
        estados = {"Pendiente": 0, "En proceso": 0, "Finalizado": 0}
        activos = {"Activas": 0, "Inactivas": 0}
        for tarea in tareas:
            if tarea.estado in estados:
                estados[tarea.estado] += 1
            if tarea.estado != "Finalizado":
                activos["Activas"] += 1
            else:
                activos["Inactivas"] += 1
        self.actualizar_pie_chart(self.chart_estado, estados, "Tareas por Estado")
        self.actualizar_pie_chart(self.chart_activa, activos, "Tareas Activas/Inactivas")

    def actualizar_pie_chart(self, chart_view, data, title):
        """
        Actualizar un gráfico de pastel.
        """
        series = QPieSeries()
        for key, value in data.items():
            slice_ = series.append(key, value)
            slice_.setLabelVisible(False)  # Ocultar etiqueta por defecto
            slice_.hovered.connect(lambda hovered, slice_=slice_: self.mostrar_tooltip(slice_, hovered))

        chart = QChart()
        chart.addSeries(series)
        chart.setTitle(title)
        chart_view.setChart(chart)

    def mostrar_tooltip(self, slice_, hovered):
        """
        Mostrar información en el gráfico al pasar el ratón.
        """
        if hovered:
            slice_.setLabelVisible(True)
            slice_.setLabelBrush(Qt.black)  # Asegurar que el texto sea negro
            slice_.setLabel(f"{slice_.label().split(':')[0]}: {slice_.value()}")
        else:
            slice_.setLabelVisible(False)

    def actualizar_resumen(self, tareas):
        total = len(tareas)
        pendientes = sum(1 for t in tareas if t.estado == "Pendiente")
        en_proceso = sum(1 for t in tareas if t.estado == "En proceso")
        finalizadas = sum(1 for t in tareas if t.estado == "Finalizado")
        self.label_resumen.setText(
            f"Número de tareas: {total}. Pendientes: {pendientes}, En proceso: {en_proceso}, Finalizadas: {finalizadas}."
        )
