# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'InicioSesion_Equipo04.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.WindowModality.NonModal)
        MainWindow.resize(904, 689)
        font = QFont()
        font.setHintingPreference(QFont.PreferDefaultHinting)
        MainWindow.setFont(font)
        MainWindow.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"QWidget#MainWindow{\n"
"        background-color: rgb(65, 130, 195);\n"
"      }")
        self.actionIniciar_sesi_n = QAction(MainWindow)
        self.actionIniciar_sesi_n.setObjectName(u"actionIniciar_sesi_n")
        font1 = QFont()
        font1.setFamilies([u"Calibri"])
        font1.setPointSize(10)
        self.actionIniciar_sesi_n.setFont(font1)
        self.actionRegistrarse = QAction(MainWindow)
        self.actionRegistrarse.setObjectName(u"actionRegistrarse")
        self.actionRegistrarse.setFont(font1)
        self.actionAcerda_de = QAction(MainWindow)
        self.actionAcerda_de.setObjectName(u"actionAcerda_de")
        self.actionNuestra_empresa = QAction(MainWindow)
        self.actionNuestra_empresa.setObjectName(u"actionNuestra_empresa")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"display:flex;\n"
"          justify-content:center;\n"
"        ")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        font2 = QFont()
        font2.setPointSize(9)
        self.frame.setFont(font2)
        self.frame.setStyleSheet(u"QWidget#frame{\n"
"                    border-radius:15px;\n"
"                    background-color: rgb(40, 81, 121);\n"
"                  }")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.labelIniciarSesion = QLabel(self.frame)
        self.labelIniciarSesion.setObjectName(u"labelIniciarSesion")
        font3 = QFont()
        font3.setFamilies([u"Segoe UI Black"])
        font3.setPointSize(29)
        font3.setHintingPreference(QFont.PreferDefaultHinting)
        self.labelIniciarSesion.setFont(font3)
        self.labelIniciarSesion.setStyleSheet(u"letter-spacing:5px;")
        self.labelIniciarSesion.setFrameShape(QFrame.Shape.NoFrame)
        self.labelIniciarSesion.setFrameShadow(QFrame.Shadow.Plain)
        self.labelIniciarSesion.setTextFormat(Qt.TextFormat.RichText)
        self.labelIniciarSesion.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout.addWidget(self.labelIniciarSesion)

        self.lineIniciarSesion = QFrame(self.frame)
        self.lineIniciarSesion.setObjectName(u"lineIniciarSesion")
        self.lineIniciarSesion.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineIniciarSesion.setFrameShape(QFrame.Shape.HLine)
        self.lineIniciarSesion.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.lineIniciarSesion)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.labelUsuario = QLabel(self.frame)
        self.labelUsuario.setObjectName(u"labelUsuario")
        font4 = QFont()
        font4.setFamilies([u"Calibri"])
        font4.setPointSize(14)
        font4.setHintingPreference(QFont.PreferDefaultHinting)
        self.labelUsuario.setFont(font4)

        self.verticalLayout.addWidget(self.labelUsuario)

        self.textoUsuarioCorreo = QLineEdit(self.frame)
        self.textoUsuarioCorreo.setObjectName(u"textoUsuarioCorreo")
        font5 = QFont()
        font5.setFamilies([u"Comic Sans"])
        font5.setPointSize(18)
        font5.setItalic(True)
        font5.setHintingPreference(QFont.PreferDefaultHinting)
        self.textoUsuarioCorreo.setFont(font5)
        self.textoUsuarioCorreo.setStyleSheet(u"background-color: #e200ff; color:black;")

        self.verticalLayout.addWidget(self.textoUsuarioCorreo)

        self.verticalSpacer_5 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        self.labelContraseña = QLabel(self.frame)
        self.labelContraseña.setObjectName(u"labelContrase\u00f1a")
        self.labelContraseña.setFont(font4)

        self.verticalLayout.addWidget(self.labelContraseña)

        self.textoContrasenna = QLineEdit(self.frame)
        self.textoContrasenna.setObjectName(u"textoContrasenna")
        self.textoContrasenna.setFont(font4)
        self.textoContrasenna.setStyleSheet(u"background-color: rgb(255, 255, 255); color:black;")
        self.textoContrasenna.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout.addWidget(self.textoContrasenna)

        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.botonIniciarSesion = QPushButton(self.frame)
        self.botonIniciarSesion.setObjectName(u"botonIniciarSesion")
        font6 = QFont()
        font6.setFamilies([u"Arial"])
        font6.setPointSize(20)
        font6.setBold(True)
        font6.setHintingPreference(QFont.PreferDefaultHinting)
        self.botonIniciarSesion.setFont(font6)
        self.botonIniciarSesion.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.botonIniciarSesion.setStyleSheet(u"background-color: #11ff00;")

        self.verticalLayout.addWidget(self.botonIniciarSesion)

        self.lineBotones = QFrame(self.frame)
        self.lineBotones.setObjectName(u"lineBotones")
        self.lineBotones.setFrameShape(QFrame.Shape.HLine)
        self.lineBotones.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.lineBotones)

        self.botonRegistrate = QPushButton(self.frame)
        self.botonRegistrate.setObjectName(u"botonRegistrate")
        font7 = QFont()
        font7.setFamilies([u"Calibri"])
        font7.setPointSize(14)
        font7.setBold(True)
        self.botonRegistrate.setFont(font7)
        self.botonRegistrate.setStyleSheet(u"background-color: #f2784b;")

        self.verticalLayout.addWidget(self.botonRegistrate)

        self.verticalSpacer_6 = QSpacerItem(20, 15, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_6)


        self.horizontalLayout.addWidget(self.frame)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 904, 33))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(40, 81, 121, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        self.menubar.setPalette(palette)
        font8 = QFont()
        font8.setFamilies([u"Arial"])
        font8.setPointSize(10)
        self.menubar.setFont(font8)
        self.menubar.setStyleSheet(u"background-color: rgb(40, 81, 121);")
        self.menuOpciones = QMenu(self.menubar)
        self.menuOpciones.setObjectName(u"menuOpciones")
        self.menuOpciones.setFont(font8)
        self.menuAcerca_de = QMenu(self.menuOpciones)
        self.menuAcerca_de.setObjectName(u"menuAcerca_de")
        self.menuIniciar_sesion = QMenu(self.menubar)
        self.menuIniciar_sesion.setObjectName(u"menuIniciar_sesion")
        self.menuRegistrarse = QMenu(self.menubar)
        self.menuRegistrarse.setObjectName(u"menuRegistrarse")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuOpciones.menuAction())
        self.menubar.addAction(self.menuRegistrarse.menuAction())
        self.menuOpciones.addAction(self.menuAcerca_de.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Inicio de sesi\u00f3n_Equipo_04", None))
        self.actionIniciar_sesi_n.setText(QCoreApplication.translate("MainWindow", u"Iniciar sesi\u00f3n", None))
        self.actionRegistrarse.setText(QCoreApplication.translate("MainWindow", u"Registrarse", None))
        self.actionAcerda_de.setText(QCoreApplication.translate("MainWindow", u"Vaciar campos de texto", None))
        self.actionNuestra_empresa.setText(QCoreApplication.translate("MainWindow", u"Nuestra empresa", None))
        self.labelIniciarSesion.setText(QCoreApplication.translate("MainWindow", u"Iniciar sesi\u00f3n", None))
        self.labelUsuario.setText(QCoreApplication.translate("MainWindow", u"Usuario/Correo", None))
        self.textoUsuarioCorreo.setText("")
        self.labelContraseña.setText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a", None))
        self.textoContrasenna.setText("")
        self.botonIniciarSesion.setText(QCoreApplication.translate("MainWindow", u"Iniciar sesi\u00f3n", None))
        self.botonRegistrate.setText(QCoreApplication.translate("MainWindow", u"Reg\u00edstrate", None))
        self.menuOpciones.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
        self.menuAcerca_de.setTitle(QCoreApplication.translate("MainWindow", u"Acerca de", None))
        self.menuIniciar_sesion.setTitle(QCoreApplication.translate("MainWindow", u"Iniciar sesi\u00f3n", None))
        self.menuRegistrarse.setTitle(QCoreApplication.translate("MainWindow", u"Reg\u00edstrate", None))
    # retranslateUi

