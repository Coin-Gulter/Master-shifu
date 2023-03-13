# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_hand_auto_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
    QPushButton, QSizePolicy, QWidget)

class Ui_dialog_hand_auto(object):
    def setupUi(self, dialog_hand_auto):
        if not dialog_hand_auto.objectName():
            dialog_hand_auto.setObjectName(u"dialog_hand_auto")
        dialog_hand_auto.resize(300, 200)
        self.dialog_hand_auto_back_frame = QFrame(dialog_hand_auto)
        self.dialog_hand_auto_back_frame.setObjectName(u"dialog_hand_auto_back_frame")
        self.dialog_hand_auto_back_frame.setGeometry(QRect(0, 0, 300, 200))
        self.dialog_hand_auto_back_frame.setStyleSheet(u".QFrame {\n"
"	\n"
"	background-color: rgb(238, 238, 238);\n"
"}")
        self.dialog_hand_auto_back_frame.setFrameShape(QFrame.StyledPanel)
        self.dialog_hand_auto_back_frame.setFrameShadow(QFrame.Raised)
        self.dialog_hand_auto_manual_button = QPushButton(self.dialog_hand_auto_back_frame)
        self.dialog_hand_auto_manual_button.setObjectName(u"dialog_hand_auto_manual_button")
        self.dialog_hand_auto_manual_button.setGeometry(QRect(38, 140, 105, 30))
        self.dialog_hand_auto_manual_button.setStyleSheet(u".QPushButton {\n"
"	background-color:  #393E46;\n"
"	color: #EEEEEE;\n"
"	font-size: 12px;\n"
"	font-weight: bold;\n"
"	border: 1px solid #393E46;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
".QPushButton:hover {\n"
"	background-color: #00ADB5;\n"
"	border-color:  #00ADB5;\n"
"}")
        self.dialog_hand_auto_auto_button = QPushButton(self.dialog_hand_auto_back_frame)
        self.dialog_hand_auto_auto_button.setObjectName(u"dialog_hand_auto_auto_button")
        self.dialog_hand_auto_auto_button.setGeometry(QRect(153, 140, 105, 30))
        self.dialog_hand_auto_auto_button.setStyleSheet(u".QPushButton {\n"
"	background-color:  #393E46;\n"
"	color: #EEEEEE;\n"
"	font-size: 12px;\n"
"	font-weight: bold;\n"
"	border: 1px solid #393E46;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
".QPushButton:hover {\n"
"	background-color: #00ADB5;\n"
"	border-color:  #00ADB5;\n"
"}")
        self.dialog_hand_auto_text_frame = QFrame(self.dialog_hand_auto_back_frame)
        self.dialog_hand_auto_text_frame.setObjectName(u"dialog_hand_auto_text_frame")
        self.dialog_hand_auto_text_frame.setGeometry(QRect(70, 25, 161, 101))
        self.dialog_hand_auto_text_frame.setStyleSheet(u".QFrame {\n"
"	border: 1px solid #c2ebec;\n"
"	border-radius: 6px;\n"
"	background-color: #c2ebec;\n"
"}")
        self.dialog_hand_auto_text_frame.setFrameShape(QFrame.StyledPanel)
        self.dialog_hand_auto_text_frame.setFrameShadow(QFrame.Raised)
        self.dialog_hand_auto_frame_label = QLabel(self.dialog_hand_auto_text_frame)
        self.dialog_hand_auto_frame_label.setObjectName(u"dialog_hand_auto_frame_label")
        self.dialog_hand_auto_frame_label.setGeometry(QRect(5, 5, 151, 91))
        self.dialog_hand_auto_frame_label.setStyleSheet(u".QLabel {\n"
"	border: 2px dashed #393E46;\n"
"	border-radius: 5px;\n"
"	padding: 40px;\n"
"}")
        self.dialog_hand_auto_text_label = QLabel(self.dialog_hand_auto_text_frame)
        self.dialog_hand_auto_text_label.setObjectName(u"dialog_hand_auto_text_label")
        self.dialog_hand_auto_text_label.setGeometry(QRect(30, 20, 101, 61))
        self.dialog_hand_auto_text_label.setStyleSheet(u".QLabel {\n"
"	font-size: 10px;\n"
"	font-weight: bold;\n"
"	text-align: center;\n"
"	color: #222831\n"
"}")

        self.retranslateUi(dialog_hand_auto)

        QMetaObject.connectSlotsByName(dialog_hand_auto)
    # setupUi

    def retranslateUi(self, dialog_hand_auto):
        dialog_hand_auto.setWindowTitle(QCoreApplication.translate("dialog_hand_auto", u"Dialog", None))
        self.dialog_hand_auto_manual_button.setText(QCoreApplication.translate("dialog_hand_auto", u"manual", None))
        self.dialog_hand_auto_auto_button.setText(QCoreApplication.translate("dialog_hand_auto", u"auto", None))
        self.dialog_hand_auto_frame_label.setText("")
        self.dialog_hand_auto_text_label.setText(QCoreApplication.translate("dialog_hand_auto", u"<html><head/><body><p><span style=\" font-size:10pt;\">Choose how you</span><br><span style=\" font-size:10pt;\">want to do it</span><br><span style=\" font-size:12pt;\">............|............</span><br><span style=\" font-size:12pt;\">...........\\/...........</span></p></body></html>", None))
    # retranslateUi

