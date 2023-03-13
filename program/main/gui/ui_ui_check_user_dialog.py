# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_check_user_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QFrame,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QStackedWidget, QWidget)
import resources_rc
import resources_rc

class Ui_Dialog_user_check(object):
    def setupUi(self, Dialog_user_check):
        if not Dialog_user_check.objectName():
            Dialog_user_check.setObjectName(u"Dialog_user_check")
        Dialog_user_check.resize(300, 200)
        Dialog_user_check.setMaximumSize(QSize(300, 200))
        self.dialog_user_check_page = QStackedWidget(Dialog_user_check)
        self.dialog_user_check_page.setObjectName(u"dialog_user_check_page")
        self.dialog_user_check_page.setGeometry(QRect(0, 0, 300, 200))
        self.page_face_id = QWidget()
        self.page_face_id.setObjectName(u"page_face_id")
        self.page_face_id_back_frame = QFrame(self.page_face_id)
        self.page_face_id_back_frame.setObjectName(u"page_face_id_back_frame")
        self.page_face_id_back_frame.setGeometry(QRect(0, 0, 300, 200))
        self.page_face_id_back_frame.setStyleSheet(u".QFrame {\n"
"	\n"
"	background-color: rgb(238, 238, 238);\n"
"}")
        self.page_face_id_back_frame.setFrameShape(QFrame.StyledPanel)
        self.page_face_id_back_frame.setFrameShadow(QFrame.Raised)
        self.page_face_id_face_animation_frame = QFrame(self.page_face_id_back_frame)
        self.page_face_id_face_animation_frame.setObjectName(u"page_face_id_face_animation_frame")
        self.page_face_id_face_animation_frame.setGeometry(QRect(50, 20, 200, 125))
        self.page_face_id_face_animation_frame.setStyleSheet(u".QFrame {\n"
"	border: 1px solid #c2ebec;\n"
"	border-radius: 6px;\n"
"	background-color: #c2ebec;\n"
"}")
        self.page_face_id_face_animation_frame.setFrameShape(QFrame.StyledPanel)
        self.page_face_id_face_animation_frame.setFrameShadow(QFrame.Raised)
        self.page_face_id_face_animation_frame_label = QLabel(self.page_face_id_face_animation_frame)
        self.page_face_id_face_animation_frame_label.setObjectName(u"page_face_id_face_animation_frame_label")
        self.page_face_id_face_animation_frame_label.setGeometry(QRect(5, 5, 190, 115))
        self.page_face_id_face_animation_frame_label.setStyleSheet(u".QLabel {\n"
"	border: 2px dashed #393E46;\n"
"	border-radius: 5px;\n"
"	padding: 40px;\n"
"}")
        self.page_face_id_face_animation_text_label = QLabel(self.page_face_id_face_animation_frame)
        self.page_face_id_face_animation_text_label.setObjectName(u"page_face_id_face_animation_text_label")
        self.page_face_id_face_animation_text_label.setGeometry(QRect(55, 90, 90, 15))
        self.page_face_id_face_animation_text_label.setStyleSheet(u".QLabel {\n"
"	font-size: 10px;\n"
"	font-weight: bold;\n"
"	text-align: center;\n"
"	color: #222831\n"
"}")
        self.page_face_id_face_animation_image_label = QLabel(self.page_face_id_face_animation_frame)
        self.page_face_id_face_animation_image_label.setObjectName(u"page_face_id_face_animation_image_label")
        self.page_face_id_face_animation_image_label.setGeometry(QRect(75, 30, 50, 40))
        self.page_face_id_face_animation_image_label.setStyleSheet(u".QLabel {\n"
"image: url(:/icons/icons/icons8-sad-96.png);\n"
"}")
        self.page_face_id_cancel_button = QPushButton(self.page_face_id_back_frame)
        self.page_face_id_cancel_button.setObjectName(u"page_face_id_cancel_button")
        self.page_face_id_cancel_button.setGeometry(QRect(40, 160, 105, 30))
        self.page_face_id_cancel_button.setStyleSheet(u".QPushButton {\n"
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
        self.page_face_id_using_password_button = QPushButton(self.page_face_id_back_frame)
        self.page_face_id_using_password_button.setObjectName(u"page_face_id_using_password_button")
        self.page_face_id_using_password_button.setGeometry(QRect(155, 160, 105, 30))
        self.page_face_id_using_password_button.setStyleSheet(u".QPushButton {\n"
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
        self.dialog_user_check_page.addWidget(self.page_face_id)
        self.page_password_check = QWidget()
        self.page_password_check.setObjectName(u"page_password_check")
        self.page_password_check_back_frame = QFrame(self.page_password_check)
        self.page_password_check_back_frame.setObjectName(u"page_password_check_back_frame")
        self.page_password_check_back_frame.setGeometry(QRect(0, 0, 300, 200))
        self.page_password_check_back_frame.setStyleSheet(u".QFrame {\n"
"	\n"
"	background-color: rgb(238, 238, 238);\n"
"}")
        self.page_password_check_back_frame.setFrameShape(QFrame.StyledPanel)
        self.page_password_check_back_frame.setFrameShadow(QFrame.Raised)
        self.page_password_check_cancel_button = QPushButton(self.page_password_check_back_frame)
        self.page_password_check_cancel_button.setObjectName(u"page_password_check_cancel_button")
        self.page_password_check_cancel_button.setGeometry(QRect(40, 150, 105, 30))
        self.page_password_check_cancel_button.setStyleSheet(u".QPushButton {\n"
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
        self.page_password_check_see_password_checkbox = QCheckBox(self.page_password_check_back_frame)
        self.page_password_check_see_password_checkbox.setObjectName(u"page_password_check_see_password_checkbox")
        self.page_password_check_see_password_checkbox.setGeometry(QRect(47, 72, 20, 20))
        self.page_password_check_see_password_checkbox.setAutoFillBackground(False)
        self.page_password_check_see_password_checkbox.setStyleSheet(u"QCheckBox {\n"
"	font-size: 10px;\n"
"	font-weight: bold;\n"
"	text-align: center;\n"
"	color: #222831\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"	height: 16px;\n"
"	width: 16px;\n"
"	border: 2px solid #393E46;\n"
"	border-radius: 3px;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"image: url(:/icons/icons/icons8-uchiha-eyes-96.png);\n"
"	background-color: #75d2d6;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"image: url(:/icons/icons/icons8-closed-eye-90.png);\n"
"	background-color: #EEEEEE;\n"
"}")
        self.page_password_check_see_password_checkbox.setIconSize(QSize(12, 12))
        self.page_password_check_see_password_checkbox.setCheckable(True)
        self.page_password_check_see_password_checkbox.setChecked(False)
        self.page_password_check_enter_password_text_label = QLabel(self.page_password_check_back_frame)
        self.page_password_check_enter_password_text_label.setObjectName(u"page_password_check_enter_password_text_label")
        self.page_password_check_enter_password_text_label.setGeometry(QRect(100, 90, 101, 61))
        self.page_password_check_enter_password_text_label.setStyleSheet(u".QLabel {\n"
"	font-size: 10px;\n"
"	font-weight: bold;\n"
"	text-align: center;\n"
"	color: #222831\n"
"}")
        self.page_password_check_enter_password_text_label.setAlignment(Qt.AlignCenter)
        self.page_password_check_animation_image_label = QLabel(self.page_password_check_back_frame)
        self.page_password_check_animation_image_label.setObjectName(u"page_password_check_animation_image_label")
        self.page_password_check_animation_image_label.setGeometry(QRect(135, 20, 31, 31))
        self.page_password_check_animation_image_label.setStyleSheet(u".QLabel {\n"
"image: url(:/icons/icons/icons8-millenium-eye-96.png);\n"
"}")
        self.page_password_check_submit_button = QPushButton(self.page_password_check_back_frame)
        self.page_password_check_submit_button.setObjectName(u"page_password_check_submit_button")
        self.page_password_check_submit_button.setGeometry(QRect(155, 150, 105, 30))
        self.page_password_check_submit_button.setStyleSheet(u".QPushButton {\n"
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
".QPushButton:pressed {\n"
"	background-color: #222831;\n"
"}")
        self.page_password_check_enter_password_line_edit = QLineEdit(self.page_password_check_back_frame)
        self.page_password_check_enter_password_line_edit.setObjectName(u"page_password_check_enter_password_line_edit")
        self.page_password_check_enter_password_line_edit.setGeometry(QRect(70, 69, 180, 25))
        self.page_password_check_enter_password_line_edit.setStyleSheet(u"QLineEdit {\n"
"	background-color:  #393E46;\n"
"     font-size: 12px;\n"
"     font-weight: bold;\n"
"     color: #EEEEEE;\n"
"     padding: 0 10px;\n"
"     border: 2px solid #222831;\n"
"     border-radius: 6px;\n"
"     selection-background-color: darkgray;\n"
"}")
        self.page_password_check_enter_password_line_edit.setEchoMode(QLineEdit.Password)
        self.page_password_check_enter_password_line_edit.setReadOnly(False)
        self.dialog_user_check_page.addWidget(self.page_password_check)

        self.retranslateUi(Dialog_user_check)

        self.dialog_user_check_page.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Dialog_user_check)
    # setupUi

    def retranslateUi(self, Dialog_user_check):
        Dialog_user_check.setWindowTitle(QCoreApplication.translate("Dialog_user_check", u"Dialog", None))
        self.page_face_id_face_animation_frame_label.setText("")
        self.page_face_id_face_animation_text_label.setText(QCoreApplication.translate("Dialog_user_check", u"Don't recognize :(", None))
        self.page_face_id_face_animation_image_label.setText("")
        self.page_face_id_cancel_button.setText(QCoreApplication.translate("Dialog_user_check", u"Cancel", None))
        self.page_face_id_using_password_button.setText(QCoreApplication.translate("Dialog_user_check", u"Using password", None))
        self.page_password_check_cancel_button.setText(QCoreApplication.translate("Dialog_user_check", u"Cancel", None))
        self.page_password_check_see_password_checkbox.setText("")
        self.page_password_check_enter_password_text_label.setText(QCoreApplication.translate("Dialog_user_check", u"<html><head/><body><p><span style=\" font-size:8pt;\">........./\\.........<br/>..........|..........<br/>Enter password</span></p></body></html>", None))
        self.page_password_check_animation_image_label.setText("")
        self.page_password_check_submit_button.setText(QCoreApplication.translate("Dialog_user_check", u"Submit", None))
        self.page_password_check_enter_password_line_edit.setText("")
    # retranslateUi

