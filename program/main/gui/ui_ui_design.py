# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_design.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QPushButton, QSizePolicy, QSlider, QStackedWidget,
    QTextEdit, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(500, 400)
        MainWindow.setMaximumSize(QSize(500, 400))
        MainWindow.setCursor(QCursor(Qt.ArrowCursor))
        MainWindow.setMouseTracking(True)
        MainWindow.setFocusPolicy(Qt.StrongFocus)
        MainWindow.setStyleSheet(u"#statusbar {\n"
"	\n"
"	background-color: rgb(0, 173, 181);\n"
"}")
        MainWindow.setDocumentMode(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.side_frame = QFrame(self.centralwidget)
        self.side_frame.setObjectName(u"side_frame")
        self.side_frame.setGeometry(QRect(0, 0, 70, 400))
        self.side_frame.setStyleSheet(u"#side_frame {\n"
"	\n"
"	background-color: rgb(57, 62, 70);\n"
"}")
        self.side_frame.setFrameShape(QFrame.StyledPanel)
        self.side_frame.setFrameShadow(QFrame.Raised)
        self.info_button = QPushButton(self.side_frame)
        self.info_button.setObjectName(u"info_button")
        self.info_button.setGeometry(QRect(10, 370, 20, 20))
        self.info_button.setStyleSheet(u".QPushButton {\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border-width: 2px;\n"
"     border-style: solid;\n"
"	border-color: #E3E3E3;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
".QPushButton:hover {\n"
"	color: rgb(200,200,200);\n"
"	background-color: rgb(0, 173, 181);\n"
"	border-width: 2px;\n"
"	border-color: #E3E3E3;\n"
"}\n"
"\n"
"\n"
".QPushButton:pressed {\n"
"    background-color: #008a90;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/icons/icons8-about-96.png", QSize(), QIcon.Normal, QIcon.Off)
        self.info_button.setIcon(icon)
        self.info_button.setIconSize(QSize(12, 12))
        self.home_button = QPushButton(self.side_frame)
        self.home_button.setObjectName(u"home_button")
        self.home_button.setGeometry(QRect(10, 100, 49, 48))
        self.home_button.setAutoFillBackground(False)
        self.home_button.setStyleSheet(u".QPushButton {\n"
"	padding: 3px;\n"
"	padding-top: 5px;\n"
"	padding-bottom: 5px;\n"
"	margin: 5px;\n"
"	background-color: #222831;\n"
"	border-width: 2px;\n"
"     border-style: solid;\n"
"	border-color: #E3E3E3;\n"
"	border-radius: 12px;\n"
"}\n"
"\n"
".QPushButton:hover {\n"
"	color: rgb(200,200,200);\n"
"	background-color: rgb(0, 173, 181);\n"
"	border-width: 2px;\n"
"	border-color: #E3E3E3;\n"
"}\n"
"\n"
".QPushButton:pressed {\n"
"    background-color: #008a90;\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/icons8-home-384.png", QSize(), QIcon.Normal, QIcon.Off)
        self.home_button.setIcon(icon1)
        self.home_button.setIconSize(QSize(24, 24))
        self.home_button.setCheckable(False)
        self.setting_button = QPushButton(self.side_frame)
        self.setting_button.setObjectName(u"setting_button")
        self.setting_button.setEnabled(True)
        self.setting_button.setGeometry(QRect(10, 150, 49, 48))
        self.setting_button.setStyleSheet(u".QPushButton {\n"
"	padding: 3px;\n"
"	padding-top: 5px;\n"
"	padding-bottom: 5px;\n"
"	margin: 5px;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border-width: 2px;\n"
"     border-style: solid;\n"
"	border-color: #E3E3E3;\n"
"	border-radius: 12px;\n"
"}\n"
"\n"
".QPushButton:hover {\n"
"	color: rgb(200,200,200);\n"
"	background-color: rgb(0, 173, 181);\n"
"	border-width: 2px;\n"
"	border-color: #E3E3E3;\n"
"}\n"
"\n"
".QPushButton:pressed {\n"
"    background-color: #008a90;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/icons8-services-96.png", QSize(), QIcon.Normal, QIcon.Off)
        self.setting_button.setIcon(icon2)
        self.setting_button.setIconSize(QSize(24, 24))
        self.extension_button = QPushButton(self.side_frame)
        self.extension_button.setObjectName(u"extension_button")
        self.extension_button.setGeometry(QRect(10, 200, 49, 48))
        self.extension_button.setStyleSheet(u".QPushButton {\n"
"	padding: 3px;\n"
"	padding-top: 5px;\n"
"	padding-bottom: 5px;\n"
"	margin: 5px;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border-width: 2px;\n"
"     border-style: solid;\n"
"	border-color: #E3E3E3;\n"
"	border-radius: 12px;\n"
"}\n"
"\n"
".QPushButton:hover {\n"
"	color: rgb(200,200,200);\n"
"	background-color: rgb(0, 173, 181);\n"
"	border-width: 2px;\n"
"	border-color: #E3E3E3;\n"
"}\n"
"\n"
".QPushButton:pressed {\n"
"    background-color: #008a90;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/icons8-puzzle-96.png", QSize(), QIcon.Normal, QIcon.Off)
        self.extension_button.setIcon(icon3)
        self.extension_button.setIconSize(QSize(24, 24))
        self.news_button = QPushButton(self.side_frame)
        self.news_button.setObjectName(u"news_button")
        self.news_button.setGeometry(QRect(10, 250, 49, 48))
        self.news_button.setStyleSheet(u".QPushButton {\n"
"	padding: 3px;\n"
"	padding-top: 5px;\n"
"	padding-bottom: 5px;\n"
"	margin: 5px;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border-width: 2px;\n"
"     border-style: solid;\n"
"	border-color: #E3E3E3;\n"
"	border-radius: 12px;\n"
"}\n"
"\n"
".QPushButton:hover {\n"
"	color: rgb(200,200,200);\n"
"	background-color: rgb(0, 173, 181);\n"
"	border-width: 2px;\n"
"	border-color: #E3E3E3;\n"
"}\n"
"\n"
".QPushButton:pressed {\n"
"    background-color: #008a90;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/icons8-scroll-144.png", QSize(), QIcon.Normal, QIcon.Off)
        self.news_button.setIcon(icon4)
        self.news_button.setIconSize(QSize(24, 24))
        self.main_frame = QFrame(self.centralwidget)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setGeometry(QRect(70, 0, 430, 400))
        self.main_frame.setStyleSheet(u"#main_frame {\n"
"	background-color: #EEEEEE;\n"
"}")
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.main_pages_widget = QStackedWidget(self.main_frame)
        self.main_pages_widget.setObjectName(u"main_pages_widget")
        self.main_pages_widget.setGeometry(QRect(0, 0, 430, 360))
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.page_home.setStyleSheet(u".QWidget {\n"
"	background-color: #EEEEEE;\n"
"}")
        self.page_home_drag_files_frame = QFrame(self.page_home)
        self.page_home_drag_files_frame.setObjectName(u"page_home_drag_files_frame")
        self.page_home_drag_files_frame.setGeometry(QRect(60, 20, 230, 130))
        self.page_home_drag_files_frame.setStyleSheet(u".QFrame {\n"
"	border: 1px solid #c2ebec;\n"
"	border-radius: 6px;\n"
"	background-color: #c2ebec;\n"
"}")
        self.page_home_drag_files_frame.setFrameShape(QFrame.StyledPanel)
        self.page_home_drag_files_frame.setFrameShadow(QFrame.Raised)
        self.drag_files_main_list_widget = QListWidget(self.page_home_drag_files_frame)
        self.drag_files_main_list_widget.setObjectName(u"drag_files_main_list_widget")
        self.drag_files_main_list_widget.setGeometry(QRect(5, 5, 220, 120))
        self.drag_files_main_list_widget.setAcceptDrops(True)
        self.drag_files_main_list_widget.setStyleSheet(u"QListWidget\n"
"{\n"
"	border : 2px dashed #393E46;\n"
"	background : #c2ebec;\n"
"	border-radius: 5px;\n"
"	font-size: 8px;\n"
"	font-weight: bold;\n"
"	color: #222831\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    border: 1px solid #00ADB5;\n"
"    border-radius: 3px;\n"
"    background: #6dcfd4;\n"
"    height: 8px;\n"
"    margin: 0px 5px 0px 5px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: #393E46;\n"
"    border-radius:2px;\n"
"    min-width: 10px;\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal,  QScrollBar::sub-page:horizontal {\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar:left-arrow:horizontal, QScrollBar::right-arrow:horizontal {\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    border: 1px solid #00ADB5;\n"
"    border-radius: 3px;\n"
"    background: #6dcfd4;\n"
"    width: 8px;\n"
"    margin: 5px 0px 5px 0px;\n"
""
                        " }\n"
" QScrollBar::handle:vertical {\n"
"    background: #393E46;\n"
"    border-radius:2px;\n"
"    min-width: 5px;\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"       background: none;\n"
" }\n"
"\n"
" QScrollBar::sub-line:vertical {\n"
"     background: none;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }")
        self.drag_files_main_list_widget.setTabKeyNavigation(False)
        self.drag_files_main_icon_label = QLabel(self.page_home_drag_files_frame)
        self.drag_files_main_icon_label.setObjectName(u"drag_files_main_icon_label")
        self.drag_files_main_icon_label.setEnabled(False)
        self.drag_files_main_icon_label.setGeometry(QRect(90, 15, 50, 50))
        self.drag_files_main_icon_label.setStyleSheet(u"image: url(:/icons/icons/icons8-25-box-384.png);")
        self.drag_files_main_text_label = QLabel(self.page_home_drag_files_frame)
        self.drag_files_main_text_label.setObjectName(u"drag_files_main_text_label")
        self.drag_files_main_text_label.setGeometry(QRect(10, 60, 211, 20))
        self.drag_files_main_text_label.setStyleSheet(u".QLabel {\n"
"	font-size: 12px;\n"
"	font-weight: bold;\n"
"	text-align: center;\n"
"	color: rgba(34, 40, 49, 125);\n"
"}")
        self.drag_files_main_text_label.setAlignment(Qt.AlignCenter)
        self.drag_files_main_browse_button = QPushButton(self.page_home_drag_files_frame)
        self.drag_files_main_browse_button.setObjectName(u"drag_files_main_browse_button")
        self.drag_files_main_browse_button.setGeometry(QRect(75, 90, 80, 20))
        self.drag_files_main_browse_button.setStyleSheet(u".QPushButton {\n"
"	background-color: rgb(57, 62, 70);\n"
"	color: #EEEEEE;\n"
"	font-size: 9px;\n"
"	font-weight: bold;\n"
"	border: 1px solid #222831;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
".QPushButton:hover {\n"
"	background-color: #00ADB5;\n"
"	border-color: #00ADB5\n"
"}\n"
"\n"
".QPushButton:pressed {\n"
"	background-color: #222831;\n"
"}")
        self.page_home_drag_folder_frame = QFrame(self.page_home)
        self.page_home_drag_folder_frame.setObjectName(u"page_home_drag_folder_frame")
        self.page_home_drag_folder_frame.setGeometry(QRect(60, 165, 230, 130))
        self.page_home_drag_folder_frame.setStyleSheet(u".QFrame {\n"
"	border: 1px solid #c2ebec;\n"
"	border-radius: 6px;\n"
"	background-color: #c2ebec;\n"
"}")
        self.page_home_drag_folder_frame.setFrameShape(QFrame.StyledPanel)
        self.page_home_drag_folder_frame.setFrameShadow(QFrame.Raised)
        self.drag_folder_main_list_widget = QListWidget(self.page_home_drag_folder_frame)
        self.drag_folder_main_list_widget.setObjectName(u"drag_folder_main_list_widget")
        self.drag_folder_main_list_widget.setGeometry(QRect(5, 5, 220, 120))
        self.drag_folder_main_list_widget.setAcceptDrops(True)
        self.drag_folder_main_list_widget.setStyleSheet(u"QListWidget\n"
"{\n"
"	border : 2px dashed #393E46;\n"
"	background : #c2ebec;\n"
"	border-radius: 5px;\n"
"	font-size: 8px;\n"
"	font-weight: bold;\n"
"	color: #222831\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    border: 1px solid #00ADB5;\n"
"    border-radius: 3px;\n"
"    background: #6dcfd4;\n"
"    height: 8px;\n"
"    margin: 0px 5px 0px 5px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: #393E46;\n"
"    border-radius:2px;\n"
"    min-width: 10px;\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal,  QScrollBar::sub-page:horizontal {\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar:left-arrow:horizontal, QScrollBar::right-arrow:horizontal {\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    border: 1px solid #00ADB5;\n"
"    border-radius: 3px;\n"
"    background: #6dcfd4;\n"
"    width: 8px;\n"
"    margin: 5px 0px 5px 0px;\n"
""
                        " }\n"
" QScrollBar::handle:vertical {\n"
"    background: #393E46;\n"
"    border-radius:2px;\n"
"    min-width: 5px;\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"       background: none;\n"
" }\n"
"\n"
" QScrollBar::sub-line:vertical {\n"
"     background: none;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }")
        self.drag_folder_main_text_label = QLabel(self.page_home_drag_folder_frame)
        self.drag_folder_main_text_label.setObjectName(u"drag_folder_main_text_label")
        self.drag_folder_main_text_label.setGeometry(QRect(9, 60, 211, 20))
        self.drag_folder_main_text_label.setStyleSheet(u".QLabel {\n"
"	font-size: 12px;\n"
"	font-weight: bold;\n"
"	text-align: center;\n"
"	color: rgba(34, 40, 49, 125);\n"
"}")
        self.drag_folder_main_text_label.setAlignment(Qt.AlignCenter)
        self.drag_folder_main_browse_button = QPushButton(self.page_home_drag_folder_frame)
        self.drag_folder_main_browse_button.setObjectName(u"drag_folder_main_browse_button")
        self.drag_folder_main_browse_button.setGeometry(QRect(75, 90, 80, 20))
        self.drag_folder_main_browse_button.setStyleSheet(u".QPushButton {\n"
"	background-color: rgb(57, 62, 70);\n"
"	color: #EEEEEE;\n"
"	font-size: 9px;\n"
"	font-weight: bold;\n"
"	border: 1px solid #222831;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
".QPushButton:hover {\n"
"	background-color: #00ADB5;\n"
"	border-color: #00ADB5\n"
"}\n"
"\n"
".QPushButton:pressed {\n"
"	background-color: #222831;\n"
"}")
        self.drag_folder_main_icon_label = QLabel(self.page_home_drag_folder_frame)
        self.drag_folder_main_icon_label.setObjectName(u"drag_folder_main_icon_label")
        self.drag_folder_main_icon_label.setGeometry(QRect(90, 10, 50, 50))
        self.drag_folder_main_icon_label.setStyleSheet(u"image: url(:/icons/icons/icons8-25-box-384.png);")
        self.page_home_encypt_button = QPushButton(self.page_home)
        self.page_home_encypt_button.setObjectName(u"page_home_encypt_button")
        self.page_home_encypt_button.setGeometry(QRect(65, 310, 100, 30))
        self.page_home_encypt_button.setStyleSheet(u".QPushButton {\n"
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
        self.page_home_decrypt_button = QPushButton(self.page_home)
        self.page_home_decrypt_button.setObjectName(u"page_home_decrypt_button")
        self.page_home_decrypt_button.setGeometry(QRect(185, 310, 100, 30))
        self.page_home_decrypt_button.setStyleSheet(u".QPushButton {\n"
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
        self.drag_files_side_label = QLabel(self.page_home)
        self.drag_files_side_label.setObjectName(u"drag_files_side_label")
        self.drag_files_side_label.setGeometry(QRect(300, 75, 120, 70))
        font = QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.drag_files_side_label.setFont(font)
        self.drag_files_side_label.setAutoFillBackground(False)
        self.drag_files_side_label.setStyleSheet(u".QLabel {\n"
"	color: #222831\n"
"}")
        self.page_home_reset_files_button = QPushButton(self.page_home)
        self.page_home_reset_files_button.setObjectName(u"page_home_reset_files_button")
        self.page_home_reset_files_button.setGeometry(QRect(310, 50, 30, 30))
        self.page_home_reset_files_button.setStyleSheet(u".QPushButton {\n"
"	background-color:  #393E46;\n"
"	color: #EEEEEE;\n"
"	font-size: 12px;\n"
"	font-weight: bold;\n"
"	border: 1px solid #393E46;\n"
"	border-radius: 5px;\n"
"	padding: 3px;\n"
"	image: url(:/icons/icons/icons8-synchronize-192#EEEEEE.png);\n"
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
        self.page_home_reset_folder_button = QPushButton(self.page_home)
        self.page_home_reset_folder_button.setObjectName(u"page_home_reset_folder_button")
        self.page_home_reset_folder_button.setGeometry(QRect(310, 195, 30, 30))
        self.page_home_reset_folder_button.setStyleSheet(u".QPushButton {\n"
"	background-color:  #393E46;\n"
"	color: #EEEEEE;\n"
"	font-size: 12px;\n"
"	font-weight: bold;\n"
"	border: 1px solid #393E46;\n"
"	border-radius: 5px;\n"
"	padding: 3px;\n"
"	image: url(:/icons/icons/icons8-synchronize-192#EEEEEE.png);\n"
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
        self.drag_folder_side_label = QLabel(self.page_home)
        self.drag_folder_side_label.setObjectName(u"drag_folder_side_label")
        self.drag_folder_side_label.setGeometry(QRect(300, 220, 120, 70))
        self.drag_folder_side_label.setFont(font)
        self.drag_folder_side_label.setAutoFillBackground(False)
        self.drag_folder_side_label.setStyleSheet(u".QLabel {\n"
"	color: #222831\n"
"}")
        self.main_pages_widget.addWidget(self.page_home)
        self.page_setting = QWidget()
        self.page_setting.setObjectName(u"page_setting")
        self.page_setting.setStyleSheet(u".QWidget {\n"
"	background-color: #EEEEEE;\n"
"}")
        self.page_setting_face_id_complexity_slider = QSlider(self.page_setting)
        self.page_setting_face_id_complexity_slider.setObjectName(u"page_setting_face_id_complexity_slider")
        self.page_setting_face_id_complexity_slider.setGeometry(QRect(60, 51, 195, 15))
        self.page_setting_face_id_complexity_slider.setMaximumSize(QSize(16777215, 16777215))
        self.page_setting_face_id_complexity_slider.setStyleSheet(u"QSlider::groove:horizontal {\n"
"border: 1px solid #393E46;\n"
"background: #EEEEEE;\n"
"height: 8px;\n"
"border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"background: #75d2d6;\n"
"border: 1px solid #393E46;\n"
"height: 10px;\n"
"border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"background: #EEEEEE;\n"
"border: 1px solid #393E46;\n"
"height: 10px;\n"
"border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"background: #222831;\n"
"border: 1px solid #222831;\n"
"width: 13px;\n"
"margin-top: -2px;\n"
"margin-bottom: -2px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"background: #00ADB5;\n"
"border: 1px solid #00ADB5;\n"
"border-radius: 3px;\n"
"}\n"
"")
        self.page_setting_face_id_complexity_slider.setSliderPosition(50)
        self.page_setting_face_id_complexity_slider.setOrientation(Qt.Horizontal)
        self.page_setting_face_id_complexity_text_label = QLabel(self.page_setting)
        self.page_setting_face_id_complexity_text_label.setObjectName(u"page_setting_face_id_complexity_text_label")
        self.page_setting_face_id_complexity_text_label.setGeometry(QRect(260, 49, 161, 16))
        self.page_setting_face_id_complexity_text_label.setStyleSheet(u".QLabel {\n"
"	font-size: 10px;\n"
"	font-weight: bold;\n"
"	text-align: center;\n"
"	color: #222831\n"
"}")
        self.page_setting_face_id_complexity_not_secure_text_label = QLabel(self.page_setting)
        self.page_setting_face_id_complexity_not_secure_text_label.setObjectName(u"page_setting_face_id_complexity_not_secure_text_label")
        self.page_setting_face_id_complexity_not_secure_text_label.setGeometry(QRect(58, 35, 70, 15))
        self.page_setting_face_id_complexity_not_secure_text_label.setStyleSheet(u".QLabel {\n"
"	font-size: 10px;\n"
"	font-weight: bold;\n"
"	text-align: center;\n"
"	color: #222831\n"
"}")
        self.page_setting_face_id_training_slider = QSlider(self.page_setting)
        self.page_setting_face_id_training_slider.setObjectName(u"page_setting_face_id_training_slider")
        self.page_setting_face_id_training_slider.setGeometry(QRect(60, 90, 195, 15))
        self.page_setting_face_id_training_slider.setMaximumSize(QSize(16777215, 16777215))
        self.page_setting_face_id_training_slider.setStyleSheet(u"QSlider::groove:horizontal {\n"
"border: 1px solid #393E46;\n"
"background: #EEEEEE;\n"
"height: 8px;\n"
"border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"background: #75d2d6;\n"
"border: 1px solid #393E46;\n"
"height: 10px;\n"
"border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"background: #EEEEEE;\n"
"border: 1px solid #393E46;\n"
"height: 10px;\n"
"border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"background: #222831;\n"
"border: 1px solid #222831;\n"
"width: 13px;\n"
"margin-top: -2px;\n"
"margin-bottom: -2px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"background: #00ADB5;\n"
"border: 1px solid #00ADB5;\n"
"border-radius: 3px;\n"
"}\n"
"")
        self.page_setting_face_id_training_slider.setSliderPosition(50)
        self.page_setting_face_id_training_slider.setOrientation(Qt.Horizontal)
        self.page_setting_face_id_training_text_label = QLabel(self.page_setting)
        self.page_setting_face_id_training_text_label.setObjectName(u"page_setting_face_id_training_text_label")
        self.page_setting_face_id_training_text_label.setGeometry(QRect(259, 88, 161, 16))
        self.page_setting_face_id_training_text_label.setStyleSheet(u".QLabel {\n"
"	font-size: 10px;\n"
"	font-weight: bold;\n"
"	text-align: center;\n"
"	color: #222831\n"
"}")
        self.page_setting_face_id_training_not_secure_text_label = QLabel(self.page_setting)
        self.page_setting_face_id_training_not_secure_text_label.setObjectName(u"page_setting_face_id_training_not_secure_text_label")
        self.page_setting_face_id_training_not_secure_text_label.setGeometry(QRect(58, 75, 60, 15))
        self.page_setting_face_id_training_not_secure_text_label.setLayoutDirection(Qt.LeftToRight)
        self.page_setting_face_id_training_not_secure_text_label.setStyleSheet(u".QLabel {\n"
"	font-size: 8px;\n"
"	font-weight: bold;\n"
"	text-align: center;\n"
"	color: #222831\n"
"}")
        self.page_setting_windows_notification_checkbox = QCheckBox(self.page_setting)
        self.page_setting_windows_notification_checkbox.setObjectName(u"page_setting_windows_notification_checkbox")
        self.page_setting_windows_notification_checkbox.setGeometry(QRect(130, 130, 210, 16))
        self.page_setting_windows_notification_checkbox.setAutoFillBackground(False)
        self.page_setting_windows_notification_checkbox.setStyleSheet(u"QCheckBox {\n"
"	font-size: 10px;\n"
"	font-weight: bold;\n"
"	text-align: center;\n"
"	color: #222831\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"	height: 12px;\n"
"	width: 12px;\n"
"	image: url(:/icons/icons/icons8-checkmark-192.png);\n"
"	background-color: #75d2d6;\n"
"	border: 1px solid #393E46;\n"
"	border-radius: 3px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"	height: 12px;\n"
"	width: 12px;\n"
"	image: url(:/icons/icons/icons8-cancel-192.png);\n"
"	background-color: #EEEEEE;\n"
"	border: 1px solid #393E46;\n"
"	border-radius: 3px;\n"
"}")
        self.page_setting_windows_notification_checkbox.setIconSize(QSize(12, 12))
        self.page_setting_windows_notification_checkbox.setCheckable(True)
        self.page_setting_windows_notification_checkbox.setChecked(True)
        self.page_setting_autostart_checkbox = QCheckBox(self.page_setting)
        self.page_setting_autostart_checkbox.setObjectName(u"page_setting_autostart_checkbox")
        self.page_setting_autostart_checkbox.setGeometry(QRect(130, 160, 210, 16))
        self.page_setting_autostart_checkbox.setAutoFillBackground(False)
        self.page_setting_autostart_checkbox.setStyleSheet(u"QCheckBox {\n"
"	font-size: 10px;\n"
"	font-weight: bold;\n"
"	text-align: center;\n"
"	color: #222831\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"	height: 12px;\n"
"	width: 12px;\n"
"	image: url(:/icons/icons/icons8-checkmark-192.png);\n"
"	background-color: #75d2d6;\n"
"	border: 1px solid #393E46;\n"
"	border-radius: 3px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"	height: 12px;\n"
"	width: 12px;\n"
"	image: url(:/icons/icons/icons8-cancel-192.png);\n"
"	background-color: #EEEEEE;\n"
"	border: 1px solid #393E46;\n"
"	border-radius: 3px;\n"
"}")
        self.page_setting_autostart_checkbox.setIconSize(QSize(12, 12))
        self.page_setting_autostart_checkbox.setCheckable(True)
        self.page_setting_autostart_checkbox.setChecked(True)
        self.page_setting_auto_face_id_always_checkbox = QCheckBox(self.page_setting)
        self.page_setting_auto_face_id_always_checkbox.setObjectName(u"page_setting_auto_face_id_always_checkbox")
        self.page_setting_auto_face_id_always_checkbox.setGeometry(QRect(130, 190, 210, 16))
        self.page_setting_auto_face_id_always_checkbox.setAutoFillBackground(False)
        self.page_setting_auto_face_id_always_checkbox.setStyleSheet(u"QCheckBox {\n"
"	font-size: 10px;\n"
"	font-weight: bold;\n"
"	text-align: center;\n"
"	color: #222831\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"	height: 12px;\n"
"	width: 12px;\n"
"	image: url(:/icons/icons/icons8-checkmark-192.png);\n"
"	background-color: #75d2d6;\n"
"	border: 1px solid #393E46;\n"
"	border-radius: 3px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"	height: 12px;\n"
"	width: 12px;\n"
"	image: url(:/icons/icons/icons8-cancel-192.png);\n"
"	background-color: #EEEEEE;\n"
"	border: 1px solid #393E46;\n"
"	border-radius: 3px;\n"
"}")
        self.page_setting_auto_face_id_always_checkbox.setIconSize(QSize(12, 12))
        self.page_setting_auto_face_id_always_checkbox.setCheckable(True)
        self.page_setting_auto_face_id_always_checkbox.setChecked(False)
        self.page_setting_face_id_overtrained_text_label = QLabel(self.page_setting)
        self.page_setting_face_id_overtrained_text_label.setObjectName(u"page_setting_face_id_overtrained_text_label")
        self.page_setting_face_id_overtrained_text_label.setGeometry(QRect(205, 75, 60, 15))
        self.page_setting_face_id_overtrained_text_label.setStyleSheet(u".QLabel {\n"
"	font-size: 8px;\n"
"	font-weight: bold;\n"
"	text-align: center;\n"
"	color: #222831\n"
"}")
        self.page_setting_submit_button = QPushButton(self.page_setting)
        self.page_setting_submit_button.setObjectName(u"page_setting_submit_button")
        self.page_setting_submit_button.setGeometry(QRect(150, 230, 100, 30))
        self.page_setting_submit_button.setStyleSheet(u".QPushButton {\n"
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
        self.main_pages_widget.addWidget(self.page_setting)
        self.page_extension = QWidget()
        self.page_extension.setObjectName(u"page_extension")
        self.page_extension.setStyleSheet(u".QWidget {\n"
"	background-color: #EEEEEE;\n"
"}")
        self.page_extension_camera_view_frame = QFrame(self.page_extension)
        self.page_extension_camera_view_frame.setObjectName(u"page_extension_camera_view_frame")
        self.page_extension_camera_view_frame.setGeometry(QRect(90, 40, 220, 220))
        self.page_extension_camera_view_frame.setStyleSheet(u".QFrame {\n"
"	border: 1px solid #c2ebec;\n"
"	border-radius: 6px;\n"
"	background-color: #c2ebec;\n"
"}")
        self.page_extension_camera_view_frame.setFrameShape(QFrame.StyledPanel)
        self.page_extension_camera_view_frame.setFrameShadow(QFrame.Raised)
        self.page_extension_camera_view_image_label = QLabel(self.page_extension_camera_view_frame)
        self.page_extension_camera_view_image_label.setObjectName(u"page_extension_camera_view_image_label")
        self.page_extension_camera_view_image_label.setGeometry(QRect(5, 5, 210, 210))
        self.page_extension_camera_view_image_label.setStyleSheet(u".QLabel {\n"
"	border: 2px dashed #393E46;\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"}")
        self.page_extension_camera_view_image_label.setPixmap(QPixmap(u":/icons/icons/icons8-picture-384.png"))
        self.page_extension_camera_view_image_label.setScaledContents(True)
        self.page_extension_camera_view_text_label = QLabel(self.page_extension_camera_view_frame)
        self.page_extension_camera_view_text_label.setObjectName(u"page_extension_camera_view_text_label")
        self.page_extension_camera_view_text_label.setGeometry(QRect(10, 190, 201, 20))
        self.page_extension_camera_view_text_label.setStyleSheet(u".QLabel {\n"
"	font-size: 10px;\n"
"	font-weight: bold;\n"
"	text-align: center;\n"
"	color: #222831\n"
"}")
        self.page_extension_camera_view_text_label.setAlignment(Qt.AlignCenter)
        self.page_extension_add_button = QPushButton(self.page_extension)
        self.page_extension_add_button.setObjectName(u"page_extension_add_button")
        self.page_extension_add_button.setEnabled(False)
        self.page_extension_add_button.setGeometry(QRect(70, 310, 100, 30))
        self.page_extension_add_button.setStyleSheet(u".QPushButton {\n"
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
        self.page_extension_reset_button = QPushButton(self.page_extension)
        self.page_extension_reset_button.setObjectName(u"page_extension_reset_button")
        self.page_extension_reset_button.setGeometry(QRect(180, 310, 30, 30))
        self.page_extension_reset_button.setStyleSheet(u".QPushButton {\n"
"	background-color:  #393E46;\n"
"	color: #EEEEEE;\n"
"	font-size: 12px;\n"
"	font-weight: bold;\n"
"	border: 1px solid #393E46;\n"
"	border-radius: 5px;\n"
"	padding: 3px;\n"
"	image: url(:/icons/icons/icons8-synchronize-192#EEEEEE.png);\n"
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
        self.page_extension_upgrade_button = QPushButton(self.page_extension)
        self.page_extension_upgrade_button.setObjectName(u"page_extension_upgrade_button")
        self.page_extension_upgrade_button.setEnabled(False)
        self.page_extension_upgrade_button.setGeometry(QRect(220, 310, 100, 30))
        self.page_extension_upgrade_button.setStyleSheet(u".QPushButton {\n"
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
        self.page_extension_registered_users_text_label = QLabel(self.page_extension)
        self.page_extension_registered_users_text_label.setObjectName(u"page_extension_registered_users_text_label")
        self.page_extension_registered_users_text_label.setGeometry(QRect(95, 20, 211, 20))
        self.page_extension_registered_users_text_label.setStyleSheet(u".QLabel {\n"
"	font-size: 10px;\n"
"	font-weight: bold;\n"
"	text-align: center;\n"
"	color: #222831\n"
"}")
        self.page_extension_registered_users_text_label.setAlignment(Qt.AlignCenter)
        self.page_extension_enter_password_line_edit = QLineEdit(self.page_extension)
        self.page_extension_enter_password_line_edit.setObjectName(u"page_extension_enter_password_line_edit")
        self.page_extension_enter_password_line_edit.setGeometry(QRect(116, 270, 180, 25))
        self.page_extension_enter_password_line_edit.setStyleSheet(u"QLineEdit {\n"
"	background-color:  #393E46;\n"
"     font-size: 12px;\n"
"     font-weight: bold;\n"
"     color: #EEEEEE;\n"
"     padding: 0 10px;\n"
"     border: 2px solid #222831;\n"
"     border-radius: 6px;\n"
"     selection-background-color: darkgray;\n"
"}")
        self.page_extension_enter_password_line_edit.setEchoMode(QLineEdit.Password)
        self.page_extension_enter_password_line_edit.setReadOnly(False)
        self.page_extension_see_password_checkbox = QCheckBox(self.page_extension)
        self.page_extension_see_password_checkbox.setObjectName(u"page_extension_see_password_checkbox")
        self.page_extension_see_password_checkbox.setGeometry(QRect(93, 272, 20, 20))
        self.page_extension_see_password_checkbox.setAutoFillBackground(False)
        self.page_extension_see_password_checkbox.setStyleSheet(u"QCheckBox {\n"
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
"	image: url(:/icons/icons/icons8-uchiha-eyes-96.png);\n"
"	background-color: #75d2d6;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"	\n"
"	image: url(:/icons/icons/icons8-closed-eye-90.png);\n"
"	background-color: #EEEEEE;\n"
"}")
        self.page_extension_see_password_checkbox.setIconSize(QSize(12, 12))
        self.page_extension_see_password_checkbox.setCheckable(True)
        self.page_extension_see_password_checkbox.setChecked(False)
        self.page_extension_camera_view_side_text_label = QLabel(self.page_extension)
        self.page_extension_camera_view_side_text_label.setObjectName(u"page_extension_camera_view_side_text_label")
        self.page_extension_camera_view_side_text_label.setGeometry(QRect(315, 120, 110, 60))
        self.page_extension_camera_view_side_text_label.setStyleSheet(u".QLabel {\n"
"	font-size: 10px;\n"
"	font-weight: bold;\n"
"	text-align: center;\n"
"	color: #222831\n"
"}")
        self.page_extension_enter_password_side_text_label = QLabel(self.page_extension)
        self.page_extension_enter_password_side_text_label.setObjectName(u"page_extension_enter_password_side_text_label")
        self.page_extension_enter_password_side_text_label.setGeometry(QRect(300, 271, 131, 20))
        self.page_extension_enter_password_side_text_label.setStyleSheet(u".QLabel {\n"
"	font-size: 10px;\n"
"	font-weight: bold;\n"
"	text-align: center;\n"
"	color: #222831\n"
"}")
        self.page_extension_enter_password_side_text_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.main_pages_widget.addWidget(self.page_extension)
        self.page_news = QWidget()
        self.page_news.setObjectName(u"page_news")
        self.page_news.setStyleSheet(u".QWidget {\n"
"	background-color: #EEEEEE;\n"
"}")
        self.page_news_news_view_frame = QFrame(self.page_news)
        self.page_news_news_view_frame.setObjectName(u"page_news_news_view_frame")
        self.page_news_news_view_frame.setGeometry(QRect(60, 80, 300, 250))
        self.page_news_news_view_frame.setStyleSheet(u".QFrame {\n"
"	border: 1px solid #c2ebec;\n"
"	border-radius: 6px;\n"
"	background-color: #c2ebec;\n"
"}")
        self.page_news_news_view_frame.setFrameShape(QFrame.StyledPanel)
        self.page_news_news_view_frame.setFrameShadow(QFrame.Raised)
        self.page_news_view_label = QLabel(self.page_news_news_view_frame)
        self.page_news_view_label.setObjectName(u"page_news_view_label")
        self.page_news_view_label.setGeometry(QRect(5, 5, 290, 240))
        self.page_news_view_label.setStyleSheet(u".QLabel {\n"
"	border: 2px dashed #393E46;\n"
"	border-radius: 5px;\n"
"	padding: 80px;\n"
"	image: url(:/icons/icons/icons8-no-synchronize-240.png);\n"
"}")
        self.page_news_text_label = QLabel(self.page_news_news_view_frame)
        self.page_news_text_label.setObjectName(u"page_news_text_label")
        self.page_news_text_label.setGeometry(QRect(125, 190, 50, 15))
        self.page_news_text_label.setStyleSheet(u".QLabel {\n"
"	font-size: 10px;\n"
"	font-weight: bold;\n"
"	text-align: center;\n"
"	color: #222831\n"
"}")
        self.page_news_server_status_frame = QFrame(self.page_news)
        self.page_news_server_status_frame.setObjectName(u"page_news_server_status_frame")
        self.page_news_server_status_frame.setGeometry(QRect(120, 25, 161, 32))
        self.page_news_server_status_frame.setStyleSheet(u".QFrame {\n"
"	border: 1px solid #c2ebec;\n"
"	border-radius: 6px;\n"
"	background-color: #c2ebec;\n"
"}")
        self.page_news_server_status_frame.setFrameShape(QFrame.StyledPanel)
        self.page_news_server_status_frame.setFrameShadow(QFrame.Raised)
        self.page_news_server_status_text_label = QLabel(self.page_news_server_status_frame)
        self.page_news_server_status_text_label.setObjectName(u"page_news_server_status_text_label")
        self.page_news_server_status_text_label.setGeometry(QRect(10, 8, 141, 16))
        self.page_news_server_status_text_label.setStyleSheet(u".QLabel {\n"
"	font-size: 10px;\n"
"	font-weight: bold;\n"
"	text-align: center;\n"
"	color: #222831\n"
"}")
        self.main_pages_widget.addWidget(self.page_news)
        self.page_info = QWidget()
        self.page_info.setObjectName(u"page_info")
        self.page_info.setStyleSheet(u".QWidget {\n"
"	background-color: #EEEEEE;\n"
"}")
        self.page_info_submit_button = QPushButton(self.page_info)
        self.page_info_submit_button.setObjectName(u"page_info_submit_button")
        self.page_info_submit_button.setGeometry(QRect(150, 305, 100, 30))
        self.page_info_submit_button.setStyleSheet(u".QPushButton {\n"
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
        self.page_info_comment_frame = QFrame(self.page_info)
        self.page_info_comment_frame.setObjectName(u"page_info_comment_frame")
        self.page_info_comment_frame.setGeometry(QRect(75, 80, 250, 200))
        self.page_info_comment_frame.setStyleSheet(u".QFrame {\n"
"	border: 1px solid #c2ebec;\n"
"	border-radius: 6px;\n"
"	background-color: #c2ebec;\n"
"}")
        self.page_info_comment_frame.setFrameShape(QFrame.StyledPanel)
        self.page_info_comment_frame.setFrameShadow(QFrame.Raised)
        self.page_info_comment_text_edit = QTextEdit(self.page_info_comment_frame)
        self.page_info_comment_text_edit.setObjectName(u"page_info_comment_text_edit")
        self.page_info_comment_text_edit.setGeometry(QRect(5, 5, 240, 190))
        self.page_info_comment_text_edit.setStyleSheet(u".QTextEdit {\n"
"	background-color:  #c2ebec;\n"
"	font-size: 12px;\n"
"	font-weight: bold;\n"
"	color: #393E46;\n"
"	padding: 0 10px;\n"
"	border: 2px dashed #393E46;\n"
"	border-radius: 6px;\n"
"	selection-background-color: darkgray;\n"
"}")
        self.page_info_side_text_label = QLabel(self.page_info)
        self.page_info_side_text_label.setObjectName(u"page_info_side_text_label")
        self.page_info_side_text_label.setGeometry(QRect(330, 170, 91, 61))
        self.page_info_side_text_label.setStyleSheet(u".QLabel {\n"
"	font-size: 10px;\n"
"	font-weight: bold;\n"
"	text-align: center;\n"
"	color: #222831\n"
"}")
        self.page_info_server_status_frame = QFrame(self.page_info)
        self.page_info_server_status_frame.setObjectName(u"page_info_server_status_frame")
        self.page_info_server_status_frame.setGeometry(QRect(120, 25, 161, 32))
        self.page_info_server_status_frame.setStyleSheet(u".QFrame {\n"
"	border: 1px solid #c2ebec;\n"
"	border-radius: 6px;\n"
"	background-color: #c2ebec;\n"
"}")
        self.page_info_server_status_frame.setFrameShape(QFrame.StyledPanel)
        self.page_info_server_status_frame.setFrameShadow(QFrame.Raised)
        self.page_info_server_status_text_label = QLabel(self.page_info_server_status_frame)
        self.page_info_server_status_text_label.setObjectName(u"page_info_server_status_text_label")
        self.page_info_server_status_text_label.setGeometry(QRect(10, 8, 141, 16))
        self.page_info_server_status_text_label.setStyleSheet(u".QLabel {\n"
"	font-size: 10px;\n"
"	font-weight: bold;\n"
"	text-align: center;\n"
"	color: #222831\n"
"}")
        self.main_pages_widget.addWidget(self.page_info)
        self.bottom_frame = QFrame(self.main_frame)
        self.bottom_frame.setObjectName(u"bottom_frame")
        self.bottom_frame.setGeometry(QRect(0, 360, 430, 40))
        self.bottom_frame.setStyleSheet(u".QFrame {\n"
"	\n"
"	background-color: #00ADB5;\n"
"}")
        self.bottom_frame.setFrameShape(QFrame.StyledPanel)
        self.bottom_frame.setFrameShadow(QFrame.Raised)
        self.version_label = QLabel(self.bottom_frame)
        self.version_label.setObjectName(u"version_label")
        self.version_label.setGeometry(QRect(350, 10, 70, 20))
        self.version_label.setStyleSheet(u".QLabel {\n"
"	font-size: 10px;\n"
"	font-weight: bold;\n"
"	text-align: center;\n"
"	color: #222831\n"
"}")
        self.version_label.setAlignment(Qt.AlignCenter)
        self.main_status_label = QLabel(self.bottom_frame)
        self.main_status_label.setObjectName(u"main_status_label")
        self.main_status_label.setGeometry(QRect(120, 10, 130, 20))
        self.main_status_label.setStyleSheet(u".QLabel {\n"
"	font-size: 10px;\n"
"	font-weight: bold;\n"
"	text-align: center;\n"
"	color: #222831\n"
"}")
        self.main_status_label.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.main_pages_widget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.info_button.setText("")
        self.home_button.setText("")
        self.setting_button.setText("")
        self.extension_button.setText("")
        self.news_button.setText("")
        self.drag_files_main_icon_label.setText("")
        self.drag_files_main_text_label.setText(QCoreApplication.translate("MainWindow", u"Browse or drag files here", None))
        self.drag_files_main_browse_button.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.drag_folder_main_text_label.setText(QCoreApplication.translate("MainWindow", u"Browse or drag folder here", None))
        self.drag_folder_main_browse_button.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.drag_folder_main_icon_label.setText("")
        self.page_home_encypt_button.setText(QCoreApplication.translate("MainWindow", u"Encrypt", None))
        self.page_home_decrypt_button.setText(QCoreApplication.translate("MainWindow", u"Decrypt", None))
        self.drag_files_side_label.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt;- Choose files that<br />     you want to<br />     encrypt or decrypt.</p></body></html>", None))
        self.page_home_reset_files_button.setText("")
        self.page_home_reset_folder_button.setText("")
        self.drag_folder_side_label.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt;- Choose place or<br />     folder where you<br />     want to put<br />     your files.</p></body></html>", None))
        self.page_setting_face_id_complexity_text_label.setText(QCoreApplication.translate("MainWindow", u"<- Face id complexity", None))
        self.page_setting_face_id_complexity_not_secure_text_label.setText(QCoreApplication.translate("MainWindow", u"|not secure|", None))
        self.page_setting_face_id_training_text_label.setText(QCoreApplication.translate("MainWindow", u"<- Face id training time", None))
        self.page_setting_face_id_training_not_secure_text_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">|</span><span style=\" font-size:6pt;\">not secure</span><span style=\" font-size:10pt;\">|</span></p></body></html>", None))
        self.page_setting_windows_notification_checkbox.setText(QCoreApplication.translate("MainWindow", u"<- Enable windows notification", None))
        self.page_setting_autostart_checkbox.setText(QCoreApplication.translate("MainWindow", u"<- Enable autostart with PC", None))
        self.page_setting_auto_face_id_always_checkbox.setText(QCoreApplication.translate("MainWindow", u"<- Enable auto face id always", None))
        self.page_setting_face_id_overtrained_text_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">|</span><span style=\" font-size:5pt;\">overtrained</span><span style=\" font-size:10pt;\">|</span></p></body></html>", None))
        self.page_setting_submit_button.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.page_extension_camera_view_image_label.setText("")
        self.page_extension_camera_view_text_label.setText(QCoreApplication.translate("MainWindow", u"Connecting to camera...", None))
        self.page_extension_add_button.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.page_extension_reset_button.setText("")
        self.page_extension_upgrade_button.setText(QCoreApplication.translate("MainWindow", u"Upgrade", None))
        self.page_extension_registered_users_text_label.setText(QCoreApplication.translate("MainWindow", u"Users not registered now", None))
        self.page_extension_enter_password_line_edit.setText("")
        self.page_extension_see_password_checkbox.setText("")
        self.page_extension_camera_view_side_text_label.setText(QCoreApplication.translate("MainWindow", u"<- No image", None))
        self.page_extension_enter_password_side_text_label.setText(QCoreApplication.translate("MainWindow", u"<- Enter password", None))
        self.page_news_view_label.setText("")
        self.page_news_text_label.setText(QCoreApplication.translate("MainWindow", u"No news", None))
        self.page_news_server_status_text_label.setText(QCoreApplication.translate("MainWindow", u"Server not available now :(", None))
        self.page_info_submit_button.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.page_info_side_text_label.setText(QCoreApplication.translate("MainWindow", u"<- Place to leave \n"
"     comment or to\n"
"     ask something", None))
        self.page_info_server_status_text_label.setText(QCoreApplication.translate("MainWindow", u"Server not available now :(", None))
        self.version_label.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:10px; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Beta v.1.0</span></p></body></html>", None))
        self.main_status_label.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:10px; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">| No users registered |</span></p></body></html>", None))
    # retranslateUi

