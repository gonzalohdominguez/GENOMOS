from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class NewGenotypeForm(object):
    def setupUi(self, NewGenotypeForm):
        if not NewGenotypeForm.objectName():
            NewGenotypeForm.setObjectName(u"NewGenotypeForm")
        NewGenotypeForm.resize(513, 706)
        self.label = QLabel(NewGenotypeForm)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 491, 31))
        self.label.setFrameShape(QFrame.WinPanel)
        self.frame = QFrame(NewGenotypeForm)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 60, 491, 151))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 90, 211, 16))
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 20, 211, 16))
        self.temperature1016LineEdit = QLineEdit(self.frame)
        self.temperature1016LineEdit.setObjectName(u"temperature1016LineEdit")
        self.temperature1016LineEdit.setGeometry(QRect(10, 50, 471, 22))
        self.temperature1534LineEdit = QLineEdit(self.frame)
        self.temperature1534LineEdit.setObjectName(u"temperature1534LineEdit")
        self.temperature1534LineEdit.setGeometry(QRect(10, 120, 471, 22))
        self.frame_2 = QFrame(NewGenotypeForm)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 220, 491, 191))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 130, 301, 16))
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 20, 301, 16))
        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 80, 301, 16))
        self.temperature1016SSLineEdit = QLineEdit(self.frame_2)
        self.temperature1016SSLineEdit.setObjectName(u"temperature1016SSLineEdit")
        self.temperature1016SSLineEdit.setGeometry(QRect(10, 50, 471, 22))
        self.temperature1016SRLineEdit = QLineEdit(self.frame_2)
        self.temperature1016SRLineEdit.setObjectName(u"temperature1016SRLineEdit")
        self.temperature1016SRLineEdit.setGeometry(QRect(10, 100, 471, 22))
        self.temperature1016RRLineEdit = QLineEdit(self.frame_2)
        self.temperature1016RRLineEdit.setObjectName(u"temperature1016RRLineEdit")
        self.temperature1016RRLineEdit.setGeometry(QRect(10, 160, 471, 22))
        self.frame_3 = QFrame(NewGenotypeForm)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(10, 430, 491, 201))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label_9 = QLabel(self.frame_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 80, 301, 16))
        self.label_7 = QLabel(self.frame_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 20, 301, 16))
        self.label_8 = QLabel(self.frame_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 140, 301, 16))
        self.temperature1534SSLineEdit = QLineEdit(self.frame_3)
        self.temperature1534SSLineEdit.setObjectName(u"temperature1534SSLineEdit")
        self.temperature1534SSLineEdit.setGeometry(QRect(10, 50, 471, 22))
        self.temperature1534SRLineEdit = QLineEdit(self.frame_3)
        self.temperature1534SRLineEdit.setObjectName(u"temperature1534SRLineEdit")
        self.temperature1534SRLineEdit.setGeometry(QRect(10, 110, 471, 22))
        self.temperature1534RRLineEdit = QLineEdit(self.frame_3)
        self.temperature1534RRLineEdit.setObjectName(u"temperature1534RRLineEdit")
        self.temperature1534RRLineEdit.setGeometry(QRect(10, 170, 471, 22))
        self.addButton = QPushButton(NewGenotypeForm)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setGeometry(QRect(90, 650, 131, 31))
        self.addButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.addButton.setStyleSheet(u"QPushButton\n"
"{	\n"
"	height: 2em;\n"
" 	border-style: solid;\n"
"	border-width: 2px;\n"
" 	border-color: #0069c0;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   	background-color:#0069c0;\n"
"	color:white;\n"
"}")
        icon = QIcon()
        icon.addFile(u"./assets/icons/add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.addButton.setIcon(icon)
        self.addButton.setIconSize(QSize(30, 30))
        self.addButton.setFlat(True)
        self.cancelButton = QPushButton(NewGenotypeForm)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setGeometry(QRect(230, 650, 131, 31))
        self.cancelButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.cancelButton.setStyleSheet(u"QPushButton\n"
"{	\n"
"	height: 2em;\n"
" 	border-style: solid;\n"
"	border-width: 2px;\n"
" 	border-color: grey;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   	background-color:grey;\n"
"	color:white;\n"
"}")
        self.cancelButton.setIconSize(QSize(30, 30))
        self.cancelButton.setFlat(True)

        self.retranslateUi(NewGenotypeForm)

        QMetaObject.connectSlotsByName(NewGenotypeForm)
    # setupUi

    def retranslateUi(self, NewGenotypeForm):
        NewGenotypeForm.setWindowTitle(QCoreApplication.translate("NewGenotypeForm", u"Nueva Muestra", None))
        self.label.setText(QCoreApplication.translate("NewGenotypeForm", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">NUEVA MUESTRA</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("NewGenotypeForm", u"<html><head/><body><p><span style=\" font-weight:600;\">Temperatura de melting (1534): </span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("NewGenotypeForm", u"<html><head/><body><p><span style=\" font-weight:600;\">Temperatura de melting (1016): </span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("NewGenotypeForm", u"<html><head/><body><p><span style=\" font-weight:600;\">Temperatura de melting est\u00e1ndar 1016 (RR): </span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("NewGenotypeForm", u"<html><head/><body><p><span style=\" font-weight:600;\">Temperatura de melting est\u00e1ndar 1016 (SS): </span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("NewGenotypeForm", u"<html><head/><body><p><span style=\" font-weight:600;\">Temperatura de melting est\u00e1ndar 1016 (SR): </span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("NewGenotypeForm", u"<html><head/><body><p><span style=\" font-weight:600;\">Temperatura de melting est\u00e1ndar 1534 (SR): </span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("NewGenotypeForm", u"<html><head/><body><p><span style=\" font-weight:600;\">Temperatura de melting est\u00e1ndar 1534 (SS): </span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("NewGenotypeForm", u"<html><head/><body><p><span style=\" font-weight:600;\">Temperatura de melting est\u00e1ndar 1534 (RR): </span></p></body></html>", None))
        self.addButton.setText(QCoreApplication.translate("NewGenotypeForm", u"AGREGAR", None))
        self.cancelButton.setText(QCoreApplication.translate("NewGenotypeForm", u"CANCELAR", None))
    # retranslateUi

