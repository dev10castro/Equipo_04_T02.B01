from PySide6.QtWidgets import QMainWindow, QMessageBox  # Importar QApplication para la app y QMainWindow para la ventana principal
from PySide6.QtCore import Slot  # Importar Slot para los decoradores de los métodos
from views.qt.qt_inicio_sesion import Ui_Inicio_Sesion_Equipo04 # Importar la clase generada a partir del archivo .ui
from views.registro_window import RegistroWindow  # Importar la clase de la ventana de registro
from controllers.usuario_controller import UsuarioController  # Importar el controlador del usuario
import webbrowser
from Componentes_Personalizado import Search_Bar
from Componentes_Personalizado import Button_Search

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
        self.barra = Search_Bar()
        self.button = Button_Search()

        # Conectar las señales (clicks de botones) con los slots (métodos) correspondientes
        self.ui.boton_iniciar_sesion.clicked.connect(self.on_button_login_clicked)
        self.ui.boton_registrate.clicked.connect(self.on_button_crear_cuenta_clicked)
        self.ui.action_nuestra_empresa.triggered.connect(self.abrirAcercaDe)
        self.ui.vaciar_campo_texto.triggered.connect(self.vaciarCamposDeTexto)
        
        self.Ui_Registro_Equipo04 = None
        self.usuario_controller = UsuarioController()
        
        
        self.ui.horizontal_Layout.addWidget(self.barra)
        self.ui.horizontal_Layout.addWidget(self.button)
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
            mensaje_error = QMessageBox(self)
            mensaje_error.setWindowTitle("Error inicio de sesión")
            mensaje_error.setText("Credenciales incorrecta")
            mensaje_error.setIcon(QMessageBox.Critical)
            mensaje_error.exec()
    
    
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
    
    """
    Método para mostrar la ventana de login cuando se cierra la de registro.
    """
    @Slot()
    def mostrar_login(self):
        # Mostrar la ventana de login
        self.show()  
    # mostrar_login
    
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
        self.ui.texto_usuario_correo.setText("")
        self.ui.texto_contrasenna.setText("")
    # vaciarCamposDeTexto