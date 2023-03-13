# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_checked_result_dialog.ui'
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
    QSizePolicy, QStackedWidget, QWidget)
import resources_rc

class Ui_dialog_checked_result(object):
    def setupUi(self, dialog_checked_result):
        if not dialog_checked_result.objectName():
            dialog_checked_result.setObjectName(u"dialog_checked_result")
        dialog_checked_result.resize(300, 200)
        self.dialog_checked_result_pages_widget = QStackedWidget(dialog_checked_result)
        self.dialog_checked_result_pages_widget.setObjectName(u"dialog_checked_result_pages_widget")
        self.dialog_checked_result_pages_widget.setGeometry(QRect(0, 0, 300, 200))
        self.page_confirmed = QWidget()
        self.page_confirmed.setObjectName(u"page_confirmed")
        self.page_confirmed_back_frame = QFrame(self.page_confirmed)
        self.page_confirmed_back_frame.setObjectName(u"page_confirmed_back_frame")
        self.page_confirmed_back_frame.setGeometry(QRect(0, 0, 300, 200))
        self.page_confirmed_back_frame.setStyleSheet(u".QFrame {\n"
"	\n"
"	background-color: rgb(238, 238, 238);\n"
"}")
        self.page_confirmed_back_frame.setFrameShape(QFrame.StyledPanel)
        self.page_confirmed_back_frame.setFrameShadow(QFrame.Raised)
        self.page_confirmed_text_frame = QFrame(self.page_confirmed_back_frame)
        self.page_confirmed_text_frame.setObjectName(u"page_confirmed_text_frame")
        self.page_confirmed_text_frame.setGeometry(QRect(50, 35, 200, 125))
        self.page_confirmed_text_frame.setStyleSheet(u".QFrame {\n"
"	border: 1px solid #c2ebec;\n"
"	border-radius: 6px;\n"
"	background-color: #c2ebec;\n"
"}")
        self.page_confirmed_text_frame.setFrameShape(QFrame.StyledPanel)
        self.page_confirmed_text_frame.setFrameShadow(QFrame.Raised)
        self.page_confirmed_label_frame = QLabel(self.page_confirmed_text_frame)
        self.page_confirmed_label_frame.setObjectName(u"page_confirmed_label_frame")
        self.page_confirmed_label_frame.setGeometry(QRect(5, 5, 190, 115))
        self.page_confirmed_label_frame.setStyleSheet(u".QLabel {\n"
"	border: 2px dashed #393E46;\n"
"	border-radius: 5px;\n"
"	padding: 40px;\n"
"}")
        self.page_confirmed_text_label = QLabel(self.page_confirmed_text_frame)
        self.page_confirmed_text_label.setObjectName(u"page_confirmed_text_label")
        self.page_confirmed_text_label.setGeometry(QRect(60, 85, 80, 21))
        self.page_confirmed_text_label.setStyleSheet(u".QLabel {\n"
"	font-size: 10px;\n"
"	font-weight: bold;\n"
"	text-align: center;\n"
"	color: #222831\n"
"}")
        self.page_confirmed_image_label = QLabel(self.page_confirmed_text_frame)
        self.page_confirmed_image_label.setObjectName(u"page_confirmed_image_label")
        self.page_confirmed_image_label.setGeometry(QRect(65, 20, 60, 60))
        self.page_confirmed_image_label.setStyleSheet(u"")
        self.page_confirmed_image_label.setPixmap(QPixmap(u":/icons/icons/icons8-checkmark-384.png"))
        self.page_confirmed_image_label.setScaledContents(True)
        self.dialog_checked_result_pages_widget.addWidget(self.page_confirmed)
        self.page_not_confirmed = QWidget()
        self.page_not_confirmed.setObjectName(u"page_not_confirmed")
        self.page_not_confirmed_back_frame = QFrame(self.page_not_confirmed)
        self.page_not_confirmed_back_frame.setObjectName(u"page_not_confirmed_back_frame")
        self.page_not_confirmed_back_frame.setGeometry(QRect(0, 0, 300, 200))
        self.page_not_confirmed_back_frame.setStyleSheet(u".QFrame {\n"
"	\n"
"	background-color: rgb(238, 238, 238);\n"
"}")
        self.page_not_confirmed_back_frame.setFrameShape(QFrame.StyledPanel)
        self.page_not_confirmed_back_frame.setFrameShadow(QFrame.Raised)
        self.page_not_confirmed_text_frame = QFrame(self.page_not_confirmed_back_frame)
        self.page_not_confirmed_text_frame.setObjectName(u"page_not_confirmed_text_frame")
        self.page_not_confirmed_text_frame.setGeometry(QRect(50, 35, 200, 125))
        self.page_not_confirmed_text_frame.setStyleSheet(u".QFrame {\n"
"	border: 1px solid #c2ebec;\n"
"	border-radius: 6px;\n"
"	background-color: #c2ebec;\n"
"}")
        self.page_not_confirmed_text_frame.setFrameShape(QFrame.StyledPanel)
        self.page_not_confirmed_text_frame.setFrameShadow(QFrame.Raised)
        self.page_not_confirmed_frame_label = QLabel(self.page_not_confirmed_text_frame)
        self.page_not_confirmed_frame_label.setObjectName(u"page_not_confirmed_frame_label")
        self.page_not_confirmed_frame_label.setGeometry(QRect(5, 5, 190, 115))
        self.page_not_confirmed_frame_label.setStyleSheet(u".QLabel {\n"
"	border: 2px dashed #393E46;\n"
"	border-radius: 5px;\n"
"	padding: 40px;\n"
"}")
        self.page_not_confirmed_text_label = QLabel(self.page_not_confirmed_text_frame)
        self.page_not_confirmed_text_label.setObjectName(u"page_not_confirmed_text_label")
        self.page_not_confirmed_text_label.setGeometry(QRect(45, 85, 100, 21))
        self.page_not_confirmed_text_label.setStyleSheet(u".QLabel {\n"
"	font-size: 10px;\n"
"	font-weight: bold;\n"
"	text-align: center;\n"
"	color: #222831\n"
"}")
        self.page_not_confirmed_image_label = QLabel(self.page_not_confirmed_text_frame)
        self.page_not_confirmed_image_label.setObjectName(u"page_not_confirmed_image_label")
        self.page_not_confirmed_image_label.setGeometry(QRect(65, 20, 60, 60))
        self.page_not_confirmed_image_label.setStyleSheet(u"")
        self.page_not_confirmed_image_label.setPixmap(QPixmap(u":/icons/icons/icons8-unavailable-384.png"))
        self.page_not_confirmed_image_label.setScaledContents(True)
        self.dialog_checked_result_pages_widget.addWidget(self.page_not_confirmed)

        self.retranslateUi(dialog_checked_result)

        self.dialog_checked_result_pages_widget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(dialog_checked_result)
    # setupUi

    def retranslateUi(self, dialog_checked_result):
        dialog_checked_result.setWindowTitle(QCoreApplication.translate("dialog_checked_result", u"Dialog", None))
        self.page_confirmed_label_frame.setText("")
        self.page_confirmed_text_label.setText(QCoreApplication.translate("dialog_checked_result", u"<html><head/><body><p><span style=\" font-size:12pt;\">Confirmed :)</span></p></body></html>", None))
        self.page_confirmed_image_label.setText("")
        self.page_not_confirmed_frame_label.setText("")
        self.page_not_confirmed_text_label.setText(QCoreApplication.translate("dialog_checked_result", u"<html><head/><body><p><span style=\" font-size:12pt;\">Not confirmed :(</span></p></body></html>", None))
        self.page_not_confirmed_image_label.setText("")
    # retranslateUi

