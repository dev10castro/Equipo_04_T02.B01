# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Registro_Equipo04.ui'
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
        MainWindow.resize(937, 922)
        font = QFont()
        font.setHintingPreference(QFont.PreferDefaultHinting)
        MainWindow.setFont(font)
        MainWindow.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"QWidget#MainWindow{\n"
"        background-color: rgb(65, 130, 195);\n"
"      }")
        self.actionIniciarSesion = QAction(MainWindow)
        self.actionIniciarSesion.setObjectName(u"actionIniciarSesion")
        font1 = QFont()
        font1.setFamilies([u"Calibri"])
        font1.setPointSize(10)
        self.actionIniciarSesion.setFont(font1)
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
        self.labelRegistro = QLabel(self.frame)
        self.labelRegistro.setObjectName(u"labelRegistro")
        font3 = QFont()
        font3.setFamilies([u"Segoe UI Black"])
        font3.setPointSize(29)
        font3.setHintingPreference(QFont.PreferDefaultHinting)
        self.labelRegistro.setFont(font3)
        self.labelRegistro.setFrameShape(QFrame.Shape.NoFrame)
        self.labelRegistro.setFrameShadow(QFrame.Shadow.Plain)
        self.labelRegistro.setTextFormat(Qt.TextFormat.RichText)
        self.labelRegistro.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout.addWidget(self.labelRegistro)

        self.lineRegistro = QFrame(self.frame)
        self.lineRegistro.setObjectName(u"lineRegistro")
        self.lineRegistro.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineRegistro.setFrameShape(QFrame.Shape.HLine)
        self.lineRegistro.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.lineRegistro)

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

        self.editUsuario = QLineEdit(self.frame)
        self.editUsuario.setObjectName(u"editUsuario")
        self.editUsuario.setFont(font4)
        self.editUsuario.setStyleSheet(u"background-color: rgb(255, 255, 255); color:black;")

        self.verticalLayout.addWidget(self.editUsuario)

        self.labelCorreo = QLabel(self.frame)
        self.labelCorreo.setObjectName(u"labelCorreo")
        self.labelCorreo.setFont(font4)

        self.verticalLayout.addWidget(self.labelCorreo)

        self.editCorreo = QLineEdit(self.frame)
        self.editCorreo.setObjectName(u"editCorreo")
        font5 = QFont()
        font5.setFamilies([u"Calibri"])
        font5.setPointSize(14)
        self.editCorreo.setFont(font5)
        self.editCorreo.setAutoFillBackground(False)
        self.editCorreo.setStyleSheet(u"background-color:white; color:black;")

        self.verticalLayout.addWidget(self.editCorreo)

        self.labelContrasenna = QLabel(self.frame)
        self.labelContrasenna.setObjectName(u"labelContrasenna")
        self.labelContrasenna.setFont(font5)

        self.verticalLayout.addWidget(self.labelContrasenna)

        self.editContrasenna = QLineEdit(self.frame)
        self.editContrasenna.setObjectName(u"editContrasenna")
        self.editContrasenna.setFont(font4)
        self.editContrasenna.setStyleSheet(u"background-color: rgb(255, 255, 255); color:black;")
        self.editContrasenna.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout.addWidget(self.editContrasenna)

        self.labelRepetirContrasenna = QLabel(self.frame)
        self.labelRepetirContrasenna.setObjectName(u"labelRepetirContrasenna")
        self.labelRepetirContrasenna.setFont(font5)

        self.verticalLayout.addWidget(self.labelRepetirContrasenna)

        self.editRContrasenna = QLineEdit(self.frame)
        self.editRContrasenna.setObjectName(u"editRContrasenna")
        self.editRContrasenna.setFont(font5)
        self.editRContrasenna.setStyleSheet(u"background-color:white; color:black;")
        self.editRContrasenna.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout.addWidget(self.editRContrasenna)

        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.btnRegistro = QPushButton(self.frame)
        self.btnRegistro.setObjectName(u"btnRegistro")
        font6 = QFont()
        font6.setFamilies([u"Calibri"])
        font6.setPointSize(14)
        font6.setBold(True)
        font6.setHintingPreference(QFont.PreferDefaultHinting)
        self.btnRegistro.setFont(font6)
        self.btnRegistro.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnRegistro.setStyleSheet(u"background-color: #f2784b;")

        self.verticalLayout.addWidget(self.btnRegistro)

        self.verticalSpacer_5 = QSpacerItem(20, 15, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_5)


        self.horizontalLayout.addWidget(self.frame)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 937, 33))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(40, 81, 121, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        self.menubar.setPalette(palette)
        font7 = QFont()
        font7.setFamilies([u"Arial"])
        font7.setPointSize(10)
        self.menubar.setFont(font7)
        self.menubar.setStyleSheet(u"background-color: rgb(40, 81, 121);")
        self.menuOpciones = QMenu(self.menubar)
        self.menuOpciones.setObjectName(u"menuOpciones")
        self.menuOpciones.setFont(font7)
        self.menuAcerca_de = QMenu(self.menuOpciones)
        self.menuAcerca_de.setObjectName(u"menuAcerca_de")
        self.menuIniciar_sesion = QMenu(self.menubar)
        self.menuIniciar_sesion.setObjectName(u"menuIniciar_sesion")
        self.menuRegistrate = QMenu(self.menubar)
        self.menuRegistrate.setObjectName(u"menuRegistrate")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuOpciones.menuAction())
        self.menubar.addAction(self.menuIniciar_sesion.menuAction())
        self.menuOpciones.addAction(self.menuAcerca_de.menuAction())
        self.menuAcerca_de.addAction(self.actionNuestra_empresa)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionIniciarSesion.setText(QCoreApplication.translate("MainWindow", u"Vaciar campos de texto", None))
        self.actionNuestra_empresa.setText(QCoreApplication.translate("MainWindow", u"Nuestra empresa", None))
        self.labelRegistro.setText(QCoreApplication.translate("MainWindow", u"Registro", None))
        self.labelUsuario.setText(QCoreApplication.translate("MainWindow", u"Usuario", None))
        self.editUsuario.setText("")
        self.labelCorreo.setText(QCoreApplication.translate("MainWindow", u"Correo", None))
        self.editCorreo.setText("")
        self.labelContrasenna.setText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a", None))
        self.editContrasenna.setText("")
        self.labelRepetirContrasenna.setText(QCoreApplication.translate("MainWindow", u"Repetir contrase\u00f1a", None))
        self.editRContrasenna.setText("")
        self.btnRegistro.setText(QCoreApplication.translate("MainWindow", u"Reg\u00edstrate", None))
        self.menuOpciones.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
        self.menuAcerca_de.setTitle(QCoreApplication.translate("MainWindow", u"Acerca de", None))
        self.menuIniciar_sesion.setTitle(QCoreApplication.translate("MainWindow", u"Iniciar sesi\u00f3n", None))
        self.menuRegistrate.setTitle(QCoreApplication.translate("MainWindow", u"Reg\u00edstrate", None))
    # retranslateUi

