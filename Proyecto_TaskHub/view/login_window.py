from PySide6.QtWidgets import QMainWindow  # Importar QApplication para la app y QMainWindow para la ventana principal
from PySide6.QtCore import Slot  # Importar Slot para los decoradores de los métodos
from PySide6.QtWidgets import QMessageBox
from view.qt.qt_inicio_sesion import Ui_Inicio_Sesion_Equipo04 # Importar la clase generada a partir del archivo .ui
from view.registro_window import RegistroWindow  # Importar la clase de la ventana de registro
from controllers.usuario_controller import UsuarioController  # Importar el controlador del usuario

class LoginWindow(QMainWindow):
    """
    Clase que representa la ventana de inicio de sesión.
    """
    def __init__(self):
        """
        Constructor que inicializa la ventana de login y sus componentes.
        """
        super().__init__()
        self.ui = Ui_Inicio_Sesion_Equipo04()
        self.ui.setupUi(self)
        
        # Conectar las señales (clicks de botones) con los slots (métodos) correspondientes
        self.ui.boton_iniciar_sesion.clicked.connect(self.on_button_login_clicked)
        self.ui.boton_registrate.clicked.connect(self.on_button_crear_cuenta_clicked);
        
        self.Ui_Registro_Equipo04 = None
        self.usuario_controller = UsuarioController()
    # __init__
    
    
    @Slot()
    def on_button_login_clicked(self):  
        print("Hemos pulsado el botón de login")
        name = self.ui.texto_usuario_correo.text()
        password = self.ui.texto_contrasenna.text()
    
    # Comprobamos de que el usuario y la contraseña existen
        if self.usuario_controller.verificar_usuario(name, password) is not None:
            print(f"Bienvenido {name}")
        
        # Crear el cuadro de diálogo de bienvenida
            mensaje_bienvenida = QMessageBox(self)
            mensaje_bienvenida.setWindowTitle("Inicio de sesión exitoso")
            mensaje_bienvenida.setText(f"Bienvenido, {name}!")
            mensaje_bienvenida.setIcon(QMessageBox.Information)
            mensaje_bienvenida.exec()
        else:
             print("Credenciales incorrectas")
    
    
    @Slot()
    def on_button_crear_cuenta_clicked(self):
        print("Hemos pulsado el botón de registro")
        self.hide()
        
        if self.Ui_Registro_Equipo04 is None:
            
            # Creamos la ventana de registro:
            self.Ui_Registro_Equipo04 = RegistroWindow(parent=self)
        
        # Mostramos la ventana de registro
        self.Ui_Registro_Equipo04.show();
        
    # on_button_crear_cuenta_clicked
    def mostrar_login(self):
        """
        Método para mostrar la ventana de login cuando se cierra la de registro.
        """
        # Mostrar la ventana de login
        self.show()  
    # mostrar_login