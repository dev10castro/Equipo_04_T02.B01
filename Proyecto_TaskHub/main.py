import sys

from PySide6.QtWidgets import QApplication

from views.login_window import LoginWindow  # Importa la clase Ui_MainWindow generada
from models import inicializacion_db as init_db

if __name__ == "__main__":
    # Creamos una instancia de QApplication, pasándole los argumentos del sistema
    app = QApplication(sys.argv)

    # Inicializamos la base de datos llamando al méto_do init_db desde el módulo inicializacion_db
    init_db.init_db()

    # Creamos una instancia de LoginWindow (la ventana de inicio de sesión)
    login_window = LoginWindow()

    # Mostramos la ventana de login
    login_window.show()

    # Ejecutamos el bucle de eventos de la aplicación para esperar interacciones del usuario
    sys.exit(app.exec()) 

# __main__