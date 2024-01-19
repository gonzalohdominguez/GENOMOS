from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class ResultsGenotypeForm(object):
    def setupUi(self, ResultsGenotypeForm):
        if not ResultsGenotypeForm.objectName():
            ResultsGenotypeForm.setObjectName(u"ResultsGenotypeForm")
        ResultsGenotypeForm.resize(634, 599)
        self.tableResults = QTableWidget(ResultsGenotypeForm)
        self.tableResults.setObjectName(u"tableResults")
        self.tableResults.setGeometry(QRect(10, 70, 611, 461))
        self.download_results = QPushButton(ResultsGenotypeForm)
        self.download_results.setObjectName(u"download_results")
        self.download_results.setGeometry(QRect(20, 550, 151, 31))
        self.download_results.setCursor(QCursor(Qt.PointingHandCursor))
        self.download_results.setStyleSheet(u"QPushButton\n"
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
        icon.addFile(u"./assets/icons/download.png", QSize(), QIcon.Normal, QIcon.Off)
        self.download_results.setIcon(icon)
        self.download_results.setIconSize(QSize(30, 30))
        self.download_results.setFlat(True)
        self.frame = QFrame(ResultsGenotypeForm)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 611, 51))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 571, 31))
        self.label.setFrameShape(QFrame.WinPanel)

        self.retranslateUi(ResultsGenotypeForm)

        QMetaObject.connectSlotsByName(ResultsGenotypeForm)
    # setupUi

    def retranslateUi(self, ResultsGenotypeForm):
        ResultsGenotypeForm.setWindowTitle(QCoreApplication.translate("ResultsGenotypeForm", u"Resultados", None))
        self.download_results.setText(QCoreApplication.translate("ResultsGenotypeForm", u"DESCARGAR", None))
        self.label.setText(QCoreApplication.translate("ResultsGenotypeForm", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">RESULTADOS</span></p></body></html>", None))
    # retranslateUi

