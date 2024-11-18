from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QTableWidget, QTableWidgetItem, QHeaderView, QCheckBox
from Componentes_Personalizado import Search_Bar, Button_Search
from PySide6.QtCore import Slot
from utils import variables
from controllers.tarea_controller import TareaController
from models.Tarea import Tarea
from PySide6.QtGui import Qt

class View_Tarea_Windows(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        # Layout principal
        self.resize(500, 500)
        self.layout_vertical_main = QVBoxLayout()
        self.setLayout(self.layout_vertical_main)  # Establecemos el layout por defecto del widget

        # Layout horizontal para barra de búsqueda
        self.layout_horizontal_search_bar = QHBoxLayout()
        self.button_search = Button_Search()
        self.search_bar = Search_Bar()

        # Creamos la tabla
        self.tabla_tarea = QTableWidget()
        self.tabla_tarea.setColumnCount(3)
        self.tabla_tarea.setHorizontalHeaderLabels(["Nombre", "Descripción", "Activa"])

        self.header = self.tabla_tarea.horizontalHeader()
        self.header.setSectionResizeMode(QHeaderView.Stretch)

        # Añadir componentes al layout horizontal
        self.layout_horizontal_search_bar.addWidget(self.search_bar)
        self.layout_horizontal_search_bar.addWidget(self.button_search)

        # Añadir layout horizontal al layout principal
        self.layout_vertical_main.addLayout(self.layout_horizontal_search_bar)
        self.layout_vertical_main.addWidget(self.tabla_tarea)

        # Variables
        self.tareas_originales = []  # Para almacenar las tareas originales sin filtrar

        # Obtener datos iniciales
        self.obtenerDatos()

        # Conectar eventos
        self.search_bar.textEdited.connect(self.cambioEnTexto)
        self.button_search.signal_presionado.connect(self.cambioEnTexto)

    def llenar_tabla(self, datos):
        """
        Llenar la tabla con los datos proporcionados.
        """
        self.tabla_tarea.setRowCount(len(datos))  # Establecer el número de filas

        for fila, datos_fila in enumerate(datos):
            for columna, dato in enumerate(datos_fila):
                if columna == 2:  # Columna "Activa"
                    checkbox = QCheckBox()
                    checkbox.setChecked(dato == "No")  # Marcar si la tarea no está activa
                    checkbox.setStyleSheet("QCheckBox::indicator { subcontrol-position: center; }")
                    checkbox.setEnabled(False)
                    self.tabla_tarea.setCellWidget(fila, columna, checkbox)
                else:
                    item = QTableWidgetItem(dato)  # Crear un QTableWidgetItem
                    #item.setTextAlignment(Qt.AlignCenter)  # Centrar el texto
                    self.tabla_tarea.setItem(fila, columna, item)  # Añadir el item a la celda correspondiente

                # Si la tarea no está activa, aplicar estilos
                if columna == 2 and dato == "No":
                    for c in range(3):  # Aplicar estilos a todas las celdas de la fila
                        item = self.tabla_tarea.item(fila, c)
                        if item:
                            item.setForeground(Qt.red)  # Color rojo
                            font = item.font()
                            font.setStrikeOut(True)  # Texto tachado
                            item.setFont(font)

   

    @Slot()
    def obtenerDatos(self):
        """
        Obtener las tareas del usuario y llenar la tabla.
        """
        try:
            # Llamar al controlador para obtener las tareas del usuario
            tareas = TareaController().obtener_tareas_por_usuario(variables.usuario)

            # Guardar las tareas originales para poder filtrar
            self.tareas_originales = tareas

            # Transformar las tareas en un formato adecuado para la tabla
            datos = [
                [tarea.nombre, tarea.descripcion, "Sí" if tarea.activa else "No"]
                for tarea in tareas
            ]

            # Llenar la tabla con los datos obtenidos
            self.llenar_tabla(datos)
        except Exception as e:
            print(f"Error al obtener las tareas: {e}")

    @Slot()
    def cambioEnTexto(self):
        """
        Actualizar la tabla en base al texto ingresado en la barra de búsqueda.
        """
        print("Se esta cambiando los datos (Boton o searchBar)")
        texto = self.search_bar.text().lower()  # Convertir a minúsculas para comparación sin distinción de mayúsculas
        tareas_filtradas = [
            tarea
            for tarea in self.tareas_originales
            if texto in tarea.nombre.lower()  # Filtrar por nombre de tarea
        ]

        # Transformar las tareas filtradas en un formato adecuado para la tabla
        datos = [
            [tarea.nombre, tarea.descripcion, "Sí" if tarea.activa else "No"]
            for tarea in tareas_filtradas
        ]

        # Llenar la tabla con los datos filtrados
        self.llenar_tabla(datos)
