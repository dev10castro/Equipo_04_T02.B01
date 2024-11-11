from PySide6.QtWidgets import QMainWindow, QMessageBox, QApplication  # Importar la clase QMainWindow para crear la ventana principal
from PySide6.QtCore import Slot  # Importar Slot para la conexión de señales y slots
from views.qt.qt_Registro import Ui_Registro_Equipo04  # Importar la clase generada a partir del archivo .ui
from controllers.usuario_controller import UsuarioController  # Importar el controlador para manejar las operaciones de registro y validación del usuario
import webbrowser

class RegistroWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)  # Llamar al constructor de la clase base QMainWindow
        self.ui = Ui_Registro_Equipo04()  # Crear una instancia de la interfaz generada
        self.ui.setupUi(self)  # Configurar la interfaz de usuario con el método setupUi

        self.ui.btn_iniciar_sesion.clicked.connect(self.function_volver_iniciar_sesion)
        self.ui.btn_registro.clicked.connect(self.function_registro)
        self.ui.vaciar_campos_de_texto.triggered.connect(self.vaciarCamposDeTexto)
        self.ui.action_nuestra_empresa_2.triggered.connect(self.abrirAcercaDe)
        
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
            mensaje_error = QMessageBox(self)
            mensaje_error.setWindowTitle("Error las contraseñas no coinciden")
            mensaje_error.setText("Error en el registro, las contraseñas no coinciden")
            mensaje_error.setIcon(QMessageBox.Critical)
            mensaje_error.exec()
            return
        
        print("Valores que se pasan a registrar_usuario:", email, nombre_usuario, password, password_confirmada)

        if self.usuario_controller.registrar_usuario(email, nombre_usuario, password, password_confirmada):
            print("usuario registrado exitosamente")
            mensaje_bienvenida = QMessageBox(self)
            mensaje_bienvenida.setWindowTitle("Registro exitoso")
            mensaje_bienvenida.setText("Usuario creado correctamente")
            mensaje_bienvenida.setIcon(QMessageBox.Information)
            mensaje_bienvenida.exec()
            self.vaciarCamposDeTexto()
        else:
            print("Error al crear el usuario")
            mensaje_error = QMessageBox(self)
            mensaje_error.setWindowTitle("Error Registro")
            mensaje_error.setText("Error al crear el usuario")
            mensaje_error.setIcon(QMessageBox.Critical)
            mensaje_error.exec()
            
            
    """
    Funcion que sirve para abrir una pagina del navegador 
    """
    @Slot()
    def abrirAcercaDe(self):
        url = "https://github.com/dev10castro/Equipo_04_T02.B01/blob/main/README.md"
        webbrowser.open(url)
    # abrirAcercaDe
    
    """
    Funcion que sirve para eliminar todo el texto que haya por pontalla en los capos de registros
    """
    @Slot()
    def vaciarCamposDeTexto(self):
        print("Borrar textos")
        self.ui.edit_contrasenna.setText("")
        self.ui.edit_correo.setText("")
        self.ui.edit_r_contrasenna.setText("")
        self.ui.edit_usuario.setText("")
    # vaciarCamposDeTexto
    
    def closeEvent(self, event):
        """Cerrar la aplicación completa al cerrar la ventana de registro."""
        QApplication.quit()