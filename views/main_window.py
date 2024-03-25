from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class ListGenotypeForm(object):
    def setupUi(self, ListGenotypeForm):
        if not ListGenotypeForm.objectName():
            ListGenotypeForm.setObjectName(u"ListGenotypeForm")
        ListGenotypeForm.resize(1098, 664)
        self.buttonsFrame = QFrame(ListGenotypeForm)
        self.buttonsFrame.setObjectName(u"buttonsFrame")
        self.buttonsFrame.setGeometry(QRect(10, 10, 1071, 91))
        self.buttonsFrame.setFrameShape(QFrame.StyledPanel)
        self.buttonsFrame.setFrameShadow(QFrame.Raised)
        self.open_new_button = QPushButton(self.buttonsFrame)
        self.open_new_button.setObjectName(u"open_new_button")
        self.open_new_button.setGeometry(QRect(30, 10, 71, 51))
        self.open_new_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.open_new_button.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#0069c0;\n"
"}")
        icon = QIcon()
        icon.addFile(u"./assets/icons/add-genotype-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.open_new_button.setIcon(icon)
        self.open_new_button.setIconSize(QSize(50, 50))
        self.open_new_button.setFlat(True)
        self.label = QLabel(self.buttonsFrame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 60, 111, 21))
        self.open_edit_button = QPushButton(self.buttonsFrame)
        self.open_edit_button.setObjectName(u"open_edit_button")
        self.open_edit_button.setGeometry(QRect(150, 10, 71, 51))
        self.open_edit_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.open_edit_button.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#0069c0;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"./assets/icons/edit-genotype.png", QSize(), QIcon.Normal, QIcon.Off)
        self.open_edit_button.setIcon(icon1)
        self.open_edit_button.setIconSize(QSize(50, 50))
        self.open_edit_button.setFlat(True)
        self.label_2 = QLabel(self.buttonsFrame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(130, 60, 111, 21))
        self.delete_genotype_button = QPushButton(self.buttonsFrame)
        self.delete_genotype_button.setObjectName(u"delete_genotype_button")
        self.delete_genotype_button.setGeometry(QRect(270, 10, 71, 51))
        self.delete_genotype_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.delete_genotype_button.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#0069c0;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"./assets/icons/delete-genotype-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.delete_genotype_button.setIcon(icon2)
        self.delete_genotype_button.setIconSize(QSize(50, 50))
        self.delete_genotype_button.setFlat(True)
        self.label_3 = QLabel(self.buttonsFrame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(250, 60, 111, 21))
        self.info_genotype_button = QPushButton(self.buttonsFrame)
        self.info_genotype_button.setObjectName(u"info_genotype_button")
        self.info_genotype_button.setGeometry(QRect(380, 10, 71, 51))
        self.info_genotype_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.info_genotype_button.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#0069c0;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"./assets/icons/info-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.info_genotype_button.setIcon(icon3)
        self.info_genotype_button.setIconSize(QSize(50, 50))
        self.info_genotype_button.setFlat(True)
        self.label_4 = QLabel(self.buttonsFrame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(370, 60, 101, 21))
        self.logo_cenexa_button = QPushButton(self.buttonsFrame)
        self.logo_cenexa_button.setObjectName(u"logo_cenexa_button")
        self.logo_cenexa_button.setGeometry(QRect(870, 10, 181, 61))
        self.logo_cenexa_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.logo_cenexa_button.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#0069c0;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"./assets/icons/logo-cenexa.png", QSize(), QIcon.Normal, QIcon.Off)
        self.logo_cenexa_button.setIcon(icon4)
        self.logo_cenexa_button.setIconSize(QSize(150, 150))
        self.logo_cenexa_button.setFlat(True)
        self.logo_creg = QPushButton(self.buttonsFrame)
        self.logo_creg.setObjectName(u"logo_creg")
        self.logo_creg.setGeometry(QRect(680, 10, 181, 61))
        self.logo_creg.setCursor(QCursor(Qt.PointingHandCursor))
        self.logo_creg.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#0069c0;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u"./assets/icons/logo creg.png", QSize(), QIcon.Normal, QIcon.Off)
        self.logo_creg.setIcon(icon5)
        self.logo_creg.setIconSize(QSize(150, 150))
        self.logo_creg.setFlat(True)
        self.frame = QFrame(ListGenotypeForm)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 110, 1071, 41))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 10, 71, 16))
        self.searchByCombobox = QComboBox(self.frame)
        self.searchByCombobox.setObjectName(u"searchByCombobox")
        self.searchByCombobox.setGeometry(QRect(90, 10, 161, 22))
        self.parameterLineEdit = QLineEdit(self.frame)
        self.parameterLineEdit.setObjectName(u"parameterLineEdit")
        self.parameterLineEdit.setGeometry(QRect(340, 10, 361, 20))
        self.searchButton = QPushButton(self.frame)
        self.searchButton.setObjectName(u"searchButton")
        self.searchButton.setGeometry(QRect(720, 10, 161, 25))
        icon6 = QIcon()
        icon6.addFile(u"./assets/icons/search-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.searchButton.setIcon(icon6)
        self.refreshButton = QPushButton(self.frame)
        self.refreshButton.setObjectName(u"refreshButton")
        self.refreshButton.setGeometry(QRect(900, 10, 161, 25))
        icon7 = QIcon()
        icon7.addFile(u"./assets/icons/refresh-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.refreshButton.setIcon(icon7)
        self.searchByCombobox_2 = QComboBox(self.frame)
        self.searchByCombobox_2.setObjectName(u"searchByCombobox_2")
        self.searchByCombobox_2.setGeometry(QRect(260, 10, 71, 22))
        self.listGenotypeTable = QTableWidget(ListGenotypeForm)
        self.listGenotypeTable.setObjectName(u"listGenotypeTable")
        self.listGenotypeTable.setGeometry(QRect(10, 230, 1071, 371))
        self.listGenotypeTable.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.listGenotypeTable.horizontalHeader().setCascadingSectionResizes(True)
        self.listGenotypeTable.horizontalHeader().setMinimumSectionSize(250)
        self.listGenotypeTable.horizontalHeader().setDefaultSectionSize(250)
        self.listGenotypeTable.horizontalHeader().setStretchLastSection(False)
        self.label_6 = QLabel(ListGenotypeForm)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 630, 131, 16))
        self.genotypesQtyLabel = QLabel(ListGenotypeForm)
        self.genotypesQtyLabel.setObjectName(u"genotypesQtyLabel")
        self.genotypesQtyLabel.setGeometry(QRect(160, 630, 55, 16))
        self.frame_2 = QFrame(ListGenotypeForm)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 160, 1071, 61))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.tabla_resultante_button = QPushButton(self.frame_2)
        self.tabla_resultante_button.setObjectName(u"tabla_resultante_button")
        self.tabla_resultante_button.setGeometry(QRect(20, 20, 151, 28))
        self.tabla_resultante_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.tabla_resultante_button.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#0069c0;\n"
"}")
        self.abrir_archivo_excel = QPushButton(self.frame_2)
        self.abrir_archivo_excel.setObjectName(u"abrir_archivo_excel")
        self.abrir_archivo_excel.setGeometry(QRect(180, 20, 151, 28))
        self.abrir_archivo_excel.setCursor(QCursor(Qt.PointingHandCursor))
        self.abrir_archivo_excel.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#0069c0;\n"
"}")
        self.guardar_archivo_excel = QPushButton(self.frame_2)
        self.guardar_archivo_excel.setObjectName(u"guardar_archivo_excel")
        self.guardar_archivo_excel.setGeometry(QRect(340, 20, 151, 28))
        self.guardar_archivo_excel.setCursor(QCursor(Qt.PointingHandCursor))
        self.guardar_archivo_excel.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#0069c0;\n"
"}")
        self.delete_datos = QPushButton(self.frame_2)
        self.delete_datos.setObjectName(u"delete_datos")
        self.delete_datos.setGeometry(QRect(500, 20, 151, 28))
        self.delete_datos.setCursor(QCursor(Qt.PointingHandCursor))
        self.delete_datos.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#0069c0;\n"
"}")

        self.retranslateUi(ListGenotypeForm)

        self.tabla_resultante_button.setDefault(True)
        self.abrir_archivo_excel.setDefault(False)
        self.guardar_archivo_excel.setDefault(False)
        self.delete_datos.setDefault(False)


        QMetaObject.connectSlotsByName(ListGenotypeForm)
    # setupUi

    def retranslateUi(self, ListGenotypeForm):
        ListGenotypeForm.setWindowTitle(QCoreApplication.translate("ListGenotypeForm", u"GENOMOS", None))
        self.open_new_button.setText("")
        self.label.setText(QCoreApplication.translate("ListGenotypeForm", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">New Sample</span></p></body></html>", None))
        self.open_edit_button.setText("")
        self.label_2.setText(QCoreApplication.translate("ListGenotypeForm", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Edit Sample</span></p></body></html>", None))
        self.delete_genotype_button.setText("")
        self.label_3.setText(QCoreApplication.translate("ListGenotypeForm", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Delete Sample</span></p></body></html>", None))
        self.info_genotype_button.setText("")
        self.label_4.setText(QCoreApplication.translate("ListGenotypeForm", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Information</span></p></body></html>", None))
        self.logo_cenexa_button.setText("")
        self.logo_creg.setText("")
        self.label_5.setText(QCoreApplication.translate("ListGenotypeForm", u"Search by:", None))
        self.searchButton.setText(QCoreApplication.translate("ListGenotypeForm", u"SEARCH", None))
        self.refreshButton.setText(QCoreApplication.translate("ListGenotypeForm", u"UPDATE", None))
        self.label_6.setText(QCoreApplication.translate("ListGenotypeForm", u"<html><head/><body><p><span style=\" font-weight:600;\">Number of records:</span></p></body></html>", None))
        self.genotypesQtyLabel.setText(QCoreApplication.translate("ListGenotypeForm", u"#", None))
        self.tabla_resultante_button.setText(QCoreApplication.translate("ListGenotypeForm", u"Results", None))
        self.abrir_archivo_excel.setText(QCoreApplication.translate("ListGenotypeForm", u"Open data", None))
        self.guardar_archivo_excel.setText(QCoreApplication.translate("ListGenotypeForm", u"Save data", None))
        self.delete_datos.setText(QCoreApplication.translate("ListGenotypeForm", u"Delete data", None))
    # retranslateUi

