# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'InicioSesion_Equipo04_V2.ui'
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

class Ui_Inicio_Sesion_Equipo04(object):
    def setupUi(self, Inicio_Sesion_Equipo04):
        if not Inicio_Sesion_Equipo04.objectName():
            Inicio_Sesion_Equipo04.setObjectName(u"Inicio_Sesion_Equipo04")
        Inicio_Sesion_Equipo04.setWindowModality(Qt.WindowModality.NonModal)
        Inicio_Sesion_Equipo04.resize(710, 601)
        font = QFont()
        font.setHintingPreference(QFont.PreferDefaultHinting)
        Inicio_Sesion_Equipo04.setFont(font)
        Inicio_Sesion_Equipo04.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        Inicio_Sesion_Equipo04.setAutoFillBackground(False)
        Inicio_Sesion_Equipo04.setStyleSheet(u"QMainWindow#Inicio_Sesion_Equipo04{\n"
"    background-color: rgb(65, 130, 195);\n"
"}")
        self.action_iniciar_sesion = QAction(Inicio_Sesion_Equipo04)
        self.action_iniciar_sesion.setObjectName(u"action_iniciar_sesion")
        font1 = QFont()
        font1.setFamilies([u"Calibri"])
        font1.setPointSize(10)
        self.action_iniciar_sesion.setFont(font1)
        self.action_registrarse = QAction(Inicio_Sesion_Equipo04)
        self.action_registrarse.setObjectName(u"action_registrarse")
        self.action_registrarse.setFont(font1)
        self.vaciar_campo_texto = QAction(Inicio_Sesion_Equipo04)
        self.vaciar_campo_texto.setObjectName(u"vaciar_campo_texto")
        self.action_nuestra_empresa = QAction(Inicio_Sesion_Equipo04)
        self.action_nuestra_empresa.setObjectName(u"action_nuestra_empresa")
        self.central_widget = QWidget(Inicio_Sesion_Equipo04)
        self.central_widget.setObjectName(u"central_widget")
        self.central_widget.setStyleSheet(u"")
        self.vertical_Layout_2 = QVBoxLayout(self.central_widget)
        self.vertical_Layout_2.setObjectName(u"vertical_Layout_2")
        self.vertical_spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vertical_Layout_2.addItem(self.vertical_spacer)

        self.horizontal_Layout = QHBoxLayout()
        self.horizontal_Layout.setObjectName(u"horizontal_Layout")
        self.horizontal_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontal_Layout.addItem(self.horizontal_spacer)

        self.frame = QFrame(self.central_widget)
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
        self.vertical_layout = QVBoxLayout(self.frame)
        self.vertical_layout.setObjectName(u"vertical_layout")
        self.label_iniciar_sesion = QLabel(self.frame)
        self.label_iniciar_sesion.setObjectName(u"label_iniciar_sesion")
        font3 = QFont()
        font3.setFamilies([u"Segoe UI Black"])
        font3.setPointSize(29)
        font3.setHintingPreference(QFont.PreferDefaultHinting)
        self.label_iniciar_sesion.setFont(font3)
        self.label_iniciar_sesion.setFrameShape(QFrame.Shape.NoFrame)
        self.label_iniciar_sesion.setFrameShadow(QFrame.Shadow.Plain)
        self.label_iniciar_sesion.setTextFormat(Qt.TextFormat.RichText)
        self.label_iniciar_sesion.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.vertical_layout.addWidget(self.label_iniciar_sesion)

        self.line_iniciar_sesion = QFrame(self.frame)
        self.line_iniciar_sesion.setObjectName(u"line_iniciar_sesion")
        self.line_iniciar_sesion.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.line_iniciar_sesion.setFrameShape(QFrame.Shape.HLine)
        self.line_iniciar_sesion.setFrameShadow(QFrame.Shadow.Sunken)

        self.vertical_layout.addWidget(self.line_iniciar_sesion)

        self.vertical_spacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vertical_layout.addItem(self.vertical_spacer_3)

        self.label_usuario = QLabel(self.frame)
        self.label_usuario.setObjectName(u"label_usuario")
        font4 = QFont()
        font4.setFamilies([u"Calibri"])
        font4.setPointSize(14)
        font4.setBold(True)
        font4.setHintingPreference(QFont.PreferDefaultHinting)
        self.label_usuario.setFont(font4)

        self.vertical_layout.addWidget(self.label_usuario)

        self.texto_usuario_correo = QLineEdit(self.frame)
        self.texto_usuario_correo.setObjectName(u"texto_usuario_correo")
        font5 = QFont()
        font5.setFamilies([u"Calibri"])
        font5.setPointSize(14)
        font5.setBold(False)
        font5.setItalic(False)
        font5.setHintingPreference(QFont.PreferDefaultHinting)
        self.texto_usuario_correo.setFont(font5)
        self.texto_usuario_correo.setStyleSheet(u"background-color: rgb(255, 255, 255); color:black;")

        self.vertical_layout.addWidget(self.texto_usuario_correo)

        self.vertical_spacer_5 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vertical_layout.addItem(self.vertical_spacer_5)

        self.label_contraseña = QLabel(self.frame)
        self.label_contraseña.setObjectName(u"label_contrase\u00f1a")
        self.label_contraseña.setFont(font4)

        self.vertical_layout.addWidget(self.label_contraseña)

        self.texto_contrasenna = QLineEdit(self.frame)
        self.texto_contrasenna.setObjectName(u"texto_contrasenna")
        font6 = QFont()
        font6.setFamilies([u"Calibri"])
        font6.setPointSize(14)
        font6.setHintingPreference(QFont.PreferDefaultHinting)
        self.texto_contrasenna.setFont(font6)
        self.texto_contrasenna.setStyleSheet(u"background-color: rgb(255, 255, 255); color:black;")
        self.texto_contrasenna.setEchoMode(QLineEdit.EchoMode.Password)

        self.vertical_layout.addWidget(self.texto_contrasenna)

        self.vertical_spacer_4 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vertical_layout.addItem(self.vertical_spacer_4)

        self.boton_iniciar_sesion = QPushButton(self.frame)
        self.boton_iniciar_sesion.setObjectName(u"boton_iniciar_sesion")
        font7 = QFont()
        font7.setFamilies([u"Calibri"])
        font7.setPointSize(20)
        font7.setBold(True)
        font7.setHintingPreference(QFont.PreferDefaultHinting)
        self.boton_iniciar_sesion.setFont(font7)
        self.boton_iniciar_sesion.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.boton_iniciar_sesion.setStyleSheet(u"background-color: #f2784b;;")
        self.boton_iniciar_sesion.setCheckable(False)
        self.boton_iniciar_sesion.setChecked(False)
        self.boton_iniciar_sesion.setAutoExclusive(False)

        self.vertical_layout.addWidget(self.boton_iniciar_sesion)

        self.line_botones = QFrame(self.frame)
        self.line_botones.setObjectName(u"line_botones")
        font8 = QFont()
        font8.setPointSize(12)
        self.line_botones.setFont(font8)
        self.line_botones.setFrameShape(QFrame.Shape.HLine)
        self.line_botones.setFrameShadow(QFrame.Shadow.Sunken)

        self.vertical_layout.addWidget(self.line_botones)

        self.boton_registrate = QPushButton(self.frame)
        self.boton_registrate.setObjectName(u"boton_registrate")
        font9 = QFont()
        font9.setFamilies([u"Calibri"])
        font9.setPointSize(20)
        font9.setBold(True)
        self.boton_registrate.setFont(font9)
        self.boton_registrate.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.boton_registrate.setStyleSheet(u"background-color: #f2784b;")
        self.boton_registrate.setCheckable(False)

        self.vertical_layout.addWidget(self.boton_registrate)

        self.vertical_spacer_6 = QSpacerItem(20, 15, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vertical_layout.addItem(self.vertical_spacer_6)


        self.horizontal_Layout.addWidget(self.frame)

        self.horizontal_spacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontal_Layout.addItem(self.horizontal_spacer_2)


        self.vertical_Layout_2.addLayout(self.horizontal_Layout)

        self.vertical_spacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vertical_Layout_2.addItem(self.vertical_spacer_2)

        Inicio_Sesion_Equipo04.setCentralWidget(self.central_widget)
        self.menubar = QMenuBar(Inicio_Sesion_Equipo04)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 710, 33))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(40, 81, 121, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.menubar.setPalette(palette)
        font10 = QFont()
        font10.setFamilies([u"Arial"])
        font10.setPointSize(10)
        self.menubar.setFont(font10)
        self.menubar.setStyleSheet(u"background-color: rgb(40, 81, 121);")
        self.menu_opciones = QMenu(self.menubar)
        self.menu_opciones.setObjectName(u"menu_opciones")
        self.menu_opciones.setFont(font10)
        self.menu_acerca_de = QMenu(self.menu_opciones)
        self.menu_acerca_de.setObjectName(u"menu_acerca_de")
        Inicio_Sesion_Equipo04.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Inicio_Sesion_Equipo04)
        self.statusbar.setObjectName(u"statusbar")
        Inicio_Sesion_Equipo04.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu_opciones.menuAction())
        self.menu_opciones.addAction(self.vaciar_campo_texto)
        self.menu_opciones.addAction(self.menu_acerca_de.menuAction())
        self.menu_acerca_de.addAction(self.action_nuestra_empresa)

        self.retranslateUi(Inicio_Sesion_Equipo04)

        QMetaObject.connectSlotsByName(Inicio_Sesion_Equipo04)
    # setupUi

    def retranslateUi(self, Inicio_Sesion_Equipo04):
        Inicio_Sesion_Equipo04.setWindowTitle(QCoreApplication.translate("Inicio_Sesion_Equipo04", u"Inicio de sesi\u00f3n_Equipo_04", None))
        self.action_iniciar_sesion.setText(QCoreApplication.translate("Inicio_Sesion_Equipo04", u"Iniciar sesi\u00f3n", None))
        self.action_registrarse.setText(QCoreApplication.translate("Inicio_Sesion_Equipo04", u"Registrarse", None))
        self.vaciar_campo_texto.setText(QCoreApplication.translate("Inicio_Sesion_Equipo04", u"Vaciar campos de texto", None))
        self.action_nuestra_empresa.setText(QCoreApplication.translate("Inicio_Sesion_Equipo04", u"Nuestra empresa", None))
        self.label_iniciar_sesion.setText(QCoreApplication.translate("Inicio_Sesion_Equipo04", u"Iniciar sesi\u00f3n", None))
        self.label_usuario.setText(QCoreApplication.translate("Inicio_Sesion_Equipo04", u"Correo", None))
        self.texto_usuario_correo.setInputMask("")
        self.texto_usuario_correo.setText("")
        self.label_contraseña.setText(QCoreApplication.translate("Inicio_Sesion_Equipo04", u"Contrase\u00f1a", None))
        self.texto_contrasenna.setText("")
        self.boton_iniciar_sesion.setText(QCoreApplication.translate("Inicio_Sesion_Equipo04", u"Iniciar sesi\u00f3n", None))
        self.boton_registrate.setText(QCoreApplication.translate("Inicio_Sesion_Equipo04", u"Reg\u00edstrate", None))
        self.menu_opciones.setTitle(QCoreApplication.translate("Inicio_Sesion_Equipo04", u"Archivo", None))
        self.menu_acerca_de.setTitle(QCoreApplication.translate("Inicio_Sesion_Equipo04", u"Acerca de", None))
    # retranslateUi

