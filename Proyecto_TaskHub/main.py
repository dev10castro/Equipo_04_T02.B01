import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from view.InicioSesion_Equipo04_uiV2 import Ui_MainWindow  # Importa la clase Ui_MainWindow generada

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Crear una instancia de la UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)  # Configura la UI en la ventana principal

if __name__ == "__main__":
    app = QApplication(sys.argv)  # Crea la aplicación
    window = MainWindow()  # Crea una instancia de la ventana
    window.show()  # Muestra la ventana
    sys.exit(app.exec())  # Ejecuta el bucle de eventos
