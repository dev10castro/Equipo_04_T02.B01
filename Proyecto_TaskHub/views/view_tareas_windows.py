from PySide6.QtWidgets import QWidget ,QHBoxLayout, QVBoxLayout, QTableWidget, QTableWidgetItem,QHeaderView
from Componentes_Personalizado import Search_Bar, Button_Search
from PySide6.QtCore import Slot
from utils import variables
from controllers.tarea_controller import TareaController
from models.Tarea import Tarea

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
        self.tabla_tarea.setHorizontalHeaderLabels(["Nombre","Descripción","Activa"])
        
        self.header = self.tabla_tarea.horizontalHeader()
        self.header.setSectionResizeMode(QHeaderView.Stretch)

  
        
        # Añadir componentes al layout horizontal
        self.layout_horizontal_search_bar.addWidget(self.search_bar)
        self.layout_horizontal_search_bar.addWidget(self.button_search)
        
        # Añadir layout horizontal al layout principal
        self.layout_vertical_main.addLayout(self.layout_horizontal_search_bar)
        self.layout_vertical_main.addWidget(self.tabla_tarea)
        
        
        # self.button_search.signal_presionado.connect(lambda: self.obtenerDatos)

        self.obtenerDatos()
        
        
        
    def llenar_tabla(self, datos):
        print(datos)
        self.tabla_tarea.setRowCount(len(datos))  # Establecer el número de filas
        
        for fila, datos_fila in enumerate(datos):
            for columna, dato in enumerate(datos_fila):
                item = QTableWidgetItem(dato)  # Crear un QTableWidgetItem
                self.tabla_tarea.setItem(fila, columna, item)  # Añadir el item a la celda correspondiente
    pass
    @Slot()
    def obtenerDatos(self):
        """
        Obtener las tareas del usuario y llenar la tabla.
        :param usuario: Nombre o identificador del usuario (correo electrónico en este caso).
        """
        try:
            # Llamar al controlador para obtener las tareas del usuario
            tareas = TareaController().obtener_tareas_por_usuario(variables.usuario)
            
            # Transformar las tareas en un formato adecuado para la tabla
            datos = [
                [tarea.nombre, tarea.descripcion, "Sí" if tarea.activa else "No"]
                for tarea in tareas
            ]
            
            # Llenar la tabla con los datos obtenidos
            self.llenar_tabla(datos)
        except Exception as e:
            print(f"Error al obtener las tareas: {e}")