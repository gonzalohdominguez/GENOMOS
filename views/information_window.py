from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class InformationForm(object):
    def setupUi(self, InformationForm):
        if not InformationForm.objectName():
            InformationForm.setObjectName(u"InformationForm")
        InformationForm.resize(855, 752)
        self.textBrowser = QTextBrowser(InformationForm)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(50, 100, 751, 511))
        self.logo_cenexa_button = QPushButton(InformationForm)
        self.logo_cenexa_button.setObjectName(u"logo_cenexa_button")
        self.logo_cenexa_button.setGeometry(QRect(430, 640, 181, 61))
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
        icon = QIcon()
        icon.addFile(u"./assets/icons/logo-cenexa.png", QSize(), QIcon.Normal, QIcon.Off)
        self.logo_cenexa_button.setIcon(icon)
        self.logo_cenexa_button.setIconSize(QSize(150, 150))
        self.logo_cenexa_button.setFlat(True)
        self.logo_creg = QPushButton(InformationForm)
        self.logo_creg.setObjectName(u"logo_creg")
        self.logo_creg.setGeometry(QRect(250, 640, 181, 61))
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
        icon1 = QIcon()
        icon1.addFile(u"./assets/icons/logo creg.png", QSize(), QIcon.Normal, QIcon.Off)
        self.logo_creg.setIcon(icon1)
        self.logo_creg.setIconSize(QSize(150, 150))
        self.logo_creg.setFlat(True)
        self.frame = QFrame(InformationForm)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 20, 831, 71))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 791, 31))
        self.label.setFrameShape(QFrame.WinPanel)
        self.label_6 = QLabel(InformationForm)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(290, 720, 251, 16))

        self.retranslateUi(InformationForm)

        QMetaObject.connectSlotsByName(InformationForm)
    # setupUi

    def retranslateUi(self, InformationForm):
        InformationForm.setWindowTitle(QCoreApplication.translate("InformationForm", u"Informaci\u00f3n", None))
        self.textBrowser.setHtml(QCoreApplication.translate("InformationForm", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; color:#9900ff;\">Welcome to GENOMOS. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; color:#9900ff;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-style:italic; color:#c300c3;\">Aedes aegypti</span><span style=\" font-size:8pt; color:#c300c3;\">, the mosquito transmitting dengue and "
                        "other viruses, is controlled with pesticides called pyrethroids. However, mutations have been identified at sites 1016 and 1534 in these insects, conferring resistance. The resulting genotype at these position can be sensitive (S), heterozygous (R1 or R2), or resistant (R1R2, R2R3, etc), depending on specific combinations of mutations at sites 1016 and 1534. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt; color:#c300c3;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; color:#aa00ff;\">The calculation of the Melting Temperature (Tm) is automatically performed in the qPCR program (Agilent Aria). This data is crucial for comparing the Tm of samples of unknown genotype with standard samples of known genotype. Examples of standard Tm are provided for each position (1016 and"
                        " 1534), which may vary between analyses. When inputting the Tm of unknown samples, the aim is to determine both the genotype for each position and the resulting genotype. For example, if a sample has a Tm of 73.3 for 1016 and 82.9 for 1534, it is inferred that the mosquito is Sensitive for 1016 and Resistant for 1534, resulting in a genotype R1R1.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt; color:#aa00ff;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt; color:#aa00ff;\"><br /></p>\n"
"<table border=\"0\" style=\" margin-top:0px; margin-bottom:0px; margin-left:8px; margin-right:0px; border-collapse:collapse;\" cellspacing=\"2\" cellpadding=\"0\" bgcolor=\"#ffffff\">\n"
"<tr>\n"
"<td style=\" vertical-align:middle; padding-left:8; padding-right:8; padding-top:"
                        "8; padding-bottom:8; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%;\"><span style=\" font-family:'Roboto','Noto','sans-serif'; font-size:8pt; font-weight:600; color:#212121;\">Allele</span></p></td>\n"
"<td style=\" vertical-align:middle; padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%;\"><span style=\" font-family:'Roboto','Noto','sans-serif'; font-size:8pt; font-weight:600; color:#212121;\">Standars</span></p></td>\n"
"<td style=\" vertical-align:middle; padding-left:8; padding-right:8; padding-top:8; padd"
                        "ing-bottom:8; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%;\"><span style=\" font-family:'Roboto','Noto','sans-serif'; font-size:8pt; font-weight:600; color:#212121;\">Tm</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:middle; padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%;\"><span style=\" font-family:'Roboto','Noto','sans-serif'; font-size:8pt; color:#212121;\">1016</span></p></td>\n"
"<td style=\" vertical-align:middle; padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top-color:#000"
                        "000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%;\"><span style=\" font-family:'Roboto','Noto','sans-serif'; font-size:8pt; color:#212121;\">SS</span></p></td>\n"
"<td style=\" vertical-align:middle; padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%;\"><span style=\" font-family:'Roboto','Noto','sans-serif'; font-size:8pt; color:#212121;\">73.36</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:middle; padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border"
                        "-left-color:#000000;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%;\"><span style=\" font-family:'Roboto','Noto','sans-serif'; font-size:8pt; color:#212121;\">1016</span></p></td>\n"
"<td style=\" vertical-align:middle; padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%;\"><span style=\" font-family:'Roboto','Noto','sans-serif'; font-size:8pt; color:#212121;\">SR</span></p></td>\n"
"<td style=\" vertical-align:middle; padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-l"
                        "eft:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%;\"><span style=\" font-family:'Roboto','Noto','sans-serif'; font-size:8pt; color:#212121;\">72.83</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:middle; padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%;\"><span style=\" font-family:'Roboto','Noto','sans-serif'; font-size:8pt; color:#212121;\">1016</span></p></td>\n"
"<td style=\" vertical-align:middle; padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; li"
                        "ne-height:100%;\"><span style=\" font-family:'Roboto','Noto','sans-serif'; font-size:8pt; color:#212121;\">RR</span></p></td>\n"
"<td style=\" vertical-align:middle; padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%;\"><span style=\" font-family:'Roboto','Noto','sans-serif'; font-size:8pt; color:#212121;\">72.55</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:middle; padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%;\"><span style=\" font-family:'Roboto','Noto','sans-s"
                        "erif'; font-size:8pt; color:#212121;\">1534</span></p></td>\n"
"<td style=\" vertical-align:middle; padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%;\"><span style=\" font-family:'Roboto','Noto','sans-serif'; font-size:8pt; color:#212121;\">SS</span></p></td>\n"
"<td style=\" vertical-align:middle; padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%;\"><span style=\" font-family:'Roboto','Noto','sans-serif'; font-size:8pt; color:#212121;\">82.23</span></p></td></tr>\n"
"<tr>\n"
"<td "
                        "style=\" vertical-align:middle; padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%;\"><span style=\" font-family:'Roboto','Noto','sans-serif'; font-size:8pt; color:#212121;\">1534</span></p></td>\n"
"<td style=\" vertical-align:middle; padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%;\"><span style=\" font-family:'Roboto','Noto','sans-serif'; font-size:8pt; color:#212121;\">SR</span></p></td>\n"
"<td style=\" vertical-align:middle; padding-left:8; padding-right:8; padding-top:8; pad"
                        "ding-bottom:8; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%;\"><span style=\" font-family:'Roboto','Noto','sans-serif'; font-size:8pt; color:#212121;\">82.5</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:middle; padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%;\"><span style=\" font-family:'Roboto','Noto','sans-serif'; font-size:8pt; color:#212121;\">1534</span></p></td>\n"
"<td style=\" vertical-align:middle; padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top-color:#000000; border-right-color:#000000"
                        "; border-bottom-color:#000000; border-left-color:#000000;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%;\"><span style=\" font-family:'Roboto','Noto','sans-serif'; font-size:8pt; color:#212121;\">RR</span></p></td>\n"
"<td style=\" vertical-align:middle; padding-left:8; padding-right:8; padding-top:8; padding-bottom:8; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%;\"><span style=\" font-family:'Roboto','Noto','sans-serif'; font-size:8pt; color:#212121;\">82.94</span></p></td></tr></table>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt; color:#aa00ff;\"><br /></p>\n"
"<p style=\" margin-top:0px; marg"
                        "in-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; color:#ff00ff;\">GENOMOS is a program that aims to recreate this process, using standard Tm as a reference to determine genotypes from the Tm of unknown samples.</span></p></body></html>", None))
        self.logo_cenexa_button.setText("")
        self.logo_creg.setText("")
        self.label.setText(QCoreApplication.translate("InformationForm", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">INFORMATION</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("InformationForm", u"<html><head/><body><p><span style=\" font-family:'arial','sans-serif'; font-size:14px; color:#4d5156;\">\u00a9 2024 GENOMOS. All rights reserved.</span></p></body></html>", None))
    # retranslateUi

