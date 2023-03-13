# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_user_result_dialog.ui'
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
import resources_rc

class Ui_Dialog_user_result(object):
    def setupUi(self, Dialog_user_result):
        if not Dialog_user_result.objectName():
            Dialog_user_result.setObjectName(u"Dialog_user_result")
        Dialog_user_result.resize(300, 200)
        Dialog_user_result.setMaximumSize(QSize(300, 200))
        self.dialog_user_result_back = QFrame(Dialog_user_result)
        self.dialog_user_result_back.setObjectName(u"dialog_user_result_back")
        self.dialog_user_result_back.setGeometry(QRect(0, 0, 300, 200))
        self.dialog_user_result_back.setStyleSheet(u".QFrame {\n"
"	\n"
"	background-color: rgb(238, 238, 238);\n"
"}")
        self.dialog_user_result_back.setFrameShape(QFrame.StyledPanel)
        self.dialog_user_result_back.setFrameShadow(QFrame.Raised)
        self.dialog_user_result_ok_button = QPushButton(self.dialog_user_result_back)
        self.dialog_user_result_ok_button.setObjectName(u"dialog_user_result_ok_button")
        self.dialog_user_result_ok_button.setGeometry(QRect(90, 160, 120, 30))
        self.dialog_user_result_ok_button.setStyleSheet(u".QPushButton {\n"
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
"}\n"
"\n"
".QPushButton:pressed {\n"
"	background-color: #222831;\n"
"}")
        self.dialog_user_result_information_back = QFrame(self.dialog_user_result_back)
        self.dialog_user_result_information_back.setObjectName(u"dialog_user_result_information_back")
        self.dialog_user_result_information_back.setGeometry(QRect(50, 20, 200, 125))
        self.dialog_user_result_information_back.setStyleSheet(u".QFrame {\n"
"	border: 1px solid #c2ebec;\n"
"	border-radius: 6px;\n"
"	background-color: #c2ebec;\n"
"}")
        self.dialog_user_result_information_back.setFrameShape(QFrame.StyledPanel)
        self.dialog_user_result_information_back.setFrameShadow(QFrame.Raised)
        self.dialog_user_result_information_frame = QLabel(self.dialog_user_result_information_back)
        self.dialog_user_result_information_frame.setObjectName(u"dialog_user_result_information_frame")
        self.dialog_user_result_information_frame.setGeometry(QRect(5, 5, 190, 115))
        self.dialog_user_result_information_frame.setStyleSheet(u".QLabel {\n"
"	border: 2px dashed #393E46;\n"
"	border-radius: 5px;\n"
"	padding: 40px;\n"
"}")
        self.dialog_user_result_information_frame_text_label = QLabel(self.dialog_user_result_information_back)
        self.dialog_user_result_information_frame_text_label.setObjectName(u"dialog_user_result_information_frame_text_label")
        self.dialog_user_result_information_frame_text_label.setGeometry(QRect(5, 80, 190, 40))
        self.dialog_user_result_information_frame_text_label.setStyleSheet(u".QLabel {\n"
"	font-size: 10px;\n"
"	font-weight: bold;\n"
"	text-align: center;\n"
"	color: #222831\n"
"}")
        self.dialog_user_result_information_frame_text_label.setAlignment(Qt.AlignCenter)
        self.dialog_user_result_information_pixmap = QLabel(self.dialog_user_result_information_back)
        self.dialog_user_result_information_pixmap.setObjectName(u"dialog_user_result_information_pixmap")
        self.dialog_user_result_information_pixmap.setGeometry(QRect(70, 20, 60, 60))
        self.dialog_user_result_information_pixmap.setStyleSheet(u"")
        self.dialog_user_result_information_pixmap.setPixmap(QPixmap(u":/icons/icons/icons8-unavailable-384.png"))
        self.dialog_user_result_information_pixmap.setScaledContents(True)

        self.retranslateUi(Dialog_user_result)

        QMetaObject.connectSlotsByName(Dialog_user_result)
    # setupUi

    def retranslateUi(self, Dialog_user_result):
        Dialog_user_result.setWindowTitle(QCoreApplication.translate("Dialog_user_result", u"Dialog", None))
        self.dialog_user_result_ok_button.setText(QCoreApplication.translate("Dialog_user_result", u"Ok", None))
        self.dialog_user_result_information_frame.setText("")
        self.dialog_user_result_information_frame_text_label.setText(QCoreApplication.translate("Dialog_user_result", u"Don't recognize :(", None))
        self.dialog_user_result_information_pixmap.setText("")
    # retranslateUi

