# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Registro_Equipo04_V2.ui'
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

class Ui_Registro_Equipo04(object):
    def setupUi(self, Registro_Equipo04):
        if not Registro_Equipo04.objectName():
            Registro_Equipo04.setObjectName(u"Registro_Equipo04")
        Registro_Equipo04.setWindowModality(Qt.WindowModality.NonModal)
        Registro_Equipo04.resize(856, 725)
        font = QFont()
        font.setHintingPreference(QFont.PreferDefaultHinting)
        Registro_Equipo04.setFont(font)
        Registro_Equipo04.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        Registro_Equipo04.setAutoFillBackground(False)
        Registro_Equipo04.setStyleSheet(u"QMainWindow#Registro_Equipo04{\n"
"    background-color: rgb(65, 130, 195);\n"
"}")
        self.action_iniciar_sesion = QAction(Registro_Equipo04)
        self.action_iniciar_sesion.setObjectName(u"action_iniciar_sesion")
        self.action_nuestra_empresa = QAction(Registro_Equipo04)
        self.action_nuestra_empresa.setObjectName(u"action_nuestra_empresa")
        self.vaciar_campos_de_texto = QAction(Registro_Equipo04)
        self.vaciar_campos_de_texto.setObjectName(u"vaciar_campos_de_texto")
        self.action_nuestra_empresa_2 = QAction(Registro_Equipo04)
        self.action_nuestra_empresa_2.setObjectName(u"action_nuestra_empresa_2")
        self.central_widget = QWidget(Registro_Equipo04)
        self.central_widget.setObjectName(u"central_widget")
        self.central_widget.setStyleSheet(u"")
        self.vertical_layout_2 = QVBoxLayout(self.central_widget)
        self.vertical_layout_2.setObjectName(u"vertical_layout_2")
        self.vertical_spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vertical_layout_2.addItem(self.vertical_spacer)

        self.horizontal_layout = QHBoxLayout()
        self.horizontal_layout.setObjectName(u"horizontal_layout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontal_layout.addItem(self.horizontalSpacer)

        self.frame = QFrame(self.central_widget)
        self.frame.setObjectName(u"frame")
        font1 = QFont()
        font1.setPointSize(9)
        self.frame.setFont(font1)
        self.frame.setStyleSheet(u"QWidget#frame{\n"
"                    border-radius:15px;\n"
"                    background-color: rgb(40, 81, 121);\n"
"                  }")
        self.frame.setFrameShape(QFrame.Shape.WinPanel)
        self.vertical_layout = QVBoxLayout(self.frame)
        self.vertical_layout.setObjectName(u"vertical_layout")
        self.label_registro = QLabel(self.frame)
        self.label_registro.setObjectName(u"label_registro")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI Black"])
        font2.setPointSize(29)
        font2.setHintingPreference(QFont.PreferDefaultHinting)
        self.label_registro.setFont(font2)
        self.label_registro.setFrameShape(QFrame.Shape.NoFrame)
        self.label_registro.setFrameShadow(QFrame.Shadow.Plain)
        self.label_registro.setTextFormat(Qt.TextFormat.RichText)
        self.label_registro.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.vertical_layout.addWidget(self.label_registro)

        self.line_registro = QFrame(self.frame)
        self.line_registro.setObjectName(u"line_registro")
        self.line_registro.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.line_registro.setFrameShape(QFrame.Shape.HLine)
        self.line_registro.setFrameShadow(QFrame.Shadow.Sunken)

        self.vertical_layout.addWidget(self.line_registro)

        self.vertical_spacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vertical_layout.addItem(self.vertical_spacer_3)

        self.label_usuario = QLabel(self.frame)
        self.label_usuario.setObjectName(u"label_usuario")
        font3 = QFont()
        font3.setFamilies([u"Calibri"])
        font3.setPointSize(14)
        font3.setBold(True)
        font3.setHintingPreference(QFont.PreferDefaultHinting)
        self.label_usuario.setFont(font3)

        self.vertical_layout.addWidget(self.label_usuario)

        self.edit_usuario = QLineEdit(self.frame)
        self.edit_usuario.setObjectName(u"edit_usuario")
        font4 = QFont()
        font4.setFamilies([u"Calibri"])
        font4.setPointSize(14)
        font4.setHintingPreference(QFont.PreferDefaultHinting)
        self.edit_usuario.setFont(font4)
        self.edit_usuario.setAutoFillBackground(False)
        self.edit_usuario.setStyleSheet(u"background-color: white; color:black;")

        self.vertical_layout.addWidget(self.edit_usuario)

        self.label_correo = QLabel(self.frame)
        self.label_correo.setObjectName(u"label_correo")
        self.label_correo.setFont(font3)

        self.vertical_layout.addWidget(self.label_correo)

        self.edit_correo = QLineEdit(self.frame)
        self.edit_correo.setObjectName(u"edit_correo")
        font5 = QFont()
        font5.setFamilies([u"Calibri"])
        font5.setPointSize(14)
        self.edit_correo.setFont(font5)
        self.edit_correo.setAutoFillBackground(False)
        self.edit_correo.setStyleSheet(u"background-color: white; color:black;")

        self.vertical_layout.addWidget(self.edit_correo)

        self.label_contrasenna = QLabel(self.frame)
        self.label_contrasenna.setObjectName(u"label_contrasenna")
        font6 = QFont()
        font6.setFamilies([u"Calibri"])
        font6.setPointSize(14)
        font6.setBold(True)
        self.label_contrasenna.setFont(font6)

        self.vertical_layout.addWidget(self.label_contrasenna)

        self.edit_contrasenna = QLineEdit(self.frame)
        self.edit_contrasenna.setObjectName(u"edit_contrasenna")
        self.edit_contrasenna.setFont(font4)
        self.edit_contrasenna.setStyleSheet(u"background-color: white; color:black;")
        self.edit_contrasenna.setEchoMode(QLineEdit.EchoMode.Password)

        self.vertical_layout.addWidget(self.edit_contrasenna)

        self.label_repetir_contrasenna = QLabel(self.frame)
        self.label_repetir_contrasenna.setObjectName(u"label_repetir_contrasenna")
        self.label_repetir_contrasenna.setFont(font6)

        self.vertical_layout.addWidget(self.label_repetir_contrasenna)

        self.edit_r_contrasenna = QLineEdit(self.frame)
        self.edit_r_contrasenna.setObjectName(u"edit_r_contrasenna")
        self.edit_r_contrasenna.setFont(font5)
        self.edit_r_contrasenna.setStyleSheet(u"background-color: white; color:black;")
        self.edit_r_contrasenna.setEchoMode(QLineEdit.EchoMode.Password)

        self.vertical_layout.addWidget(self.edit_r_contrasenna)

        self.vertical_spacer_4 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vertical_layout.addItem(self.vertical_spacer_4)

        self.btn_registro = QPushButton(self.frame)
        self.btn_registro.setObjectName(u"btn_registro")
        font7 = QFont()
        font7.setFamilies([u"Calibri"])
        font7.setPointSize(20)
        font7.setBold(True)
        font7.setKerning(False)
        font7.setHintingPreference(QFont.PreferDefaultHinting)
        self.btn_registro.setFont(font7)
        self.btn_registro.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_registro.setStyleSheet(u"background-color: #f2784b;")

        self.vertical_layout.addWidget(self.btn_registro)

        self.line = QFrame(self.frame)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.vertical_layout.addWidget(self.line)

        self.btn_iniciar_sesion = QPushButton(self.frame)
        self.btn_iniciar_sesion.setObjectName(u"btn_iniciar_sesion")
        font8 = QFont()
        font8.setFamilies([u"Calibri"])
        font8.setPointSize(20)
        font8.setBold(True)
        font8.setItalic(False)
        font8.setHintingPreference(QFont.PreferDefaultHinting)
        self.btn_iniciar_sesion.setFont(font8)
        self.btn_iniciar_sesion.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_iniciar_sesion.setStyleSheet(u"background-color: #f2784b")

        self.vertical_layout.addWidget(self.btn_iniciar_sesion)

        self.vertical_spacer_5 = QSpacerItem(20, 15, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vertical_layout.addItem(self.vertical_spacer_5)


        self.horizontal_layout.addWidget(self.frame)

        self.horizontal_spacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontal_layout.addItem(self.horizontal_spacer_2)


        self.vertical_layout_2.addLayout(self.horizontal_layout)

        self.vertical_spacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vertical_layout_2.addItem(self.vertical_spacer_2)

        Registro_Equipo04.setCentralWidget(self.central_widget)
        self.menubar = QMenuBar(Registro_Equipo04)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 856, 33))
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
        self.menubar.setAutoFillBackground(False)
        self.menubar.setStyleSheet(u"background-color: rgb(40, 81, 121);")
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        self.menu_acerca_de = QMenu(self.menuArchivo)
        self.menu_acerca_de.setObjectName(u"menu_acerca_de")
        Registro_Equipo04.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Registro_Equipo04)
        self.statusbar.setObjectName(u"statusbar")
        Registro_Equipo04.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menuArchivo.addAction(self.vaciar_campos_de_texto)
        self.menuArchivo.addAction(self.menu_acerca_de.menuAction())
        self.menu_acerca_de.addAction(self.action_nuestra_empresa_2)

        self.retranslateUi(Registro_Equipo04)

        QMetaObject.connectSlotsByName(Registro_Equipo04)
    # setupUi

    def retranslateUi(self, Registro_Equipo04):
        Registro_Equipo04.setWindowTitle(QCoreApplication.translate("Registro_Equipo04", u"Registro Equipo_04", None))
        self.action_iniciar_sesion.setText(QCoreApplication.translate("Registro_Equipo04", u"Vaciar campos de texto", None))
        self.action_nuestra_empresa.setText(QCoreApplication.translate("Registro_Equipo04", u"Nuestra empresa", None))
        self.vaciar_campos_de_texto.setText(QCoreApplication.translate("Registro_Equipo04", u"Vaciar campos de texto", None))
        self.action_nuestra_empresa_2.setText(QCoreApplication.translate("Registro_Equipo04", u"Nuestra empresa", None))
        self.label_registro.setText(QCoreApplication.translate("Registro_Equipo04", u"Registro", None))
        self.label_usuario.setText(QCoreApplication.translate("Registro_Equipo04", u"Usuario", None))
        self.edit_usuario.setText("")
        self.label_correo.setText(QCoreApplication.translate("Registro_Equipo04", u"Correo", None))
        self.edit_correo.setText("")
        self.label_contrasenna.setText(QCoreApplication.translate("Registro_Equipo04", u"Contrase\u00f1a", None))
        self.edit_contrasenna.setText("")
        self.label_repetir_contrasenna.setText(QCoreApplication.translate("Registro_Equipo04", u"Repetir contrase\u00f1a", None))
        self.edit_r_contrasenna.setText("")
        self.btn_registro.setText(QCoreApplication.translate("Registro_Equipo04", u"Reg\u00edstrate", None))
        self.btn_iniciar_sesion.setText(QCoreApplication.translate("Registro_Equipo04", u"Iniciar sesi\u00f3n", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("Registro_Equipo04", u"Archivo", None))
        self.menu_acerca_de.setTitle(QCoreApplication.translate("Registro_Equipo04", u"Acerca de", None))
    # retranslateUi

