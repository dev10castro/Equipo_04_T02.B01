from PySide6.QtWidgets import QMainWindow  # Importar la clase QMainWindow para crear la ventana principal
from PySide6.QtCore import Slot  # Importar Slot para la conexión de señales y slots
from view.qt.qt_Registro import Ui_Registro_Equipo04  # Importar la clase generada a partir del archivo .ui
from controllers.usuario_controller import UsuarioController  # Importar el controlador para manejar las operaciones de registro y validación del usuario

class RegistroWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)  # Llamar al constructor de la clase base QMainWindow
        self.ui = Ui_Registro_Equipo04()  # Crear una instancia de la interfaz generada
        self.ui.setupUi(self)  # Configurar la interfaz de usuario con el método setupUi

        self.ui.btn_iniciar_sesion.clicked.connect(self.function_volver_iniciar_sesion)
        
        self.ui.btn_registro.clicked.connect(self.function_registro)
        
        self.usuario_controller = UsuarioController()
    # __init__
    
    @Slot()
    def function_volver_iniciar_sesion(self):
        self.hide()
        
        if self.parent() is not None:
            self.parent().mostrar_login()
        
    @Slot()
    def function_registro(self):

        nombre_usuario = self.ui.edit_usuario.text()
        email = self.ui.edit_correo.text()
        password = self.ui.edit_contrasenna.text()
        password_confirmada = self.ui.edit_r_contrasenna.text()
        
        if password != password_confirmada:
            print("Las contraseñas no coinciden")
            return
        
        print("Valores que se pasan a registrar_usuario:", email, nombre_usuario, password, password_confirmada)

        if self.usuario_controller.registrar_usuario(email, nombre_usuario, password, password_confirmada):
            print("usuario registrado exitosamente")
        else:
            print("Error al crear el usuario")