# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui_manual_auto_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dialog_hand_auto(object):
    def setupUi(self, dialog_hand_auto):
        dialog_hand_auto.setObjectName("dialog_hand_auto")
        dialog_hand_auto.resize(300, 200)
        dialog_hand_auto.setMinimumSize(QtCore.QSize(300, 200))
        dialog_hand_auto.setMaximumSize(QtCore.QSize(300, 200))
        self.dialog_hand_auto_back_frame = QtWidgets.QFrame(dialog_hand_auto)
        self.dialog_hand_auto_back_frame.setGeometry(QtCore.QRect(0, 0, 300, 200))
        self.dialog_hand_auto_back_frame.setStyleSheet(".QFrame {\n"
"    \n"
"    background-color: rgb(238, 238, 238);\n"
"}")
        self.dialog_hand_auto_back_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.dialog_hand_auto_back_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.dialog_hand_auto_back_frame.setObjectName("dialog_hand_auto_back_frame")
        self.dialog_hand_auto_manual_button = QtWidgets.QPushButton(self.dialog_hand_auto_back_frame)
        self.dialog_hand_auto_manual_button.setGeometry(QtCore.QRect(38, 140, 105, 30))
        self.dialog_hand_auto_manual_button.setStyleSheet(".QPushButton {\n"
"    background-color:  #393E46;\n"
"    color: #EEEEEE;\n"
"    font-size: 12px;\n"
"    font-weight: bold;\n"
"    border: 1px solid #393E46;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
".QPushButton:hover {\n"
"    background-color: #00ADB5;\n"
"    border-color:  #00ADB5;\n"
"}\n"
".QPushButton:pressed {\n"
"    background-color: #222831;\n"
"}")
        self.dialog_hand_auto_manual_button.setObjectName("dialog_hand_auto_manual_button")
        self.dialog_hand_auto_auto_button = QtWidgets.QPushButton(self.dialog_hand_auto_back_frame)
        self.dialog_hand_auto_auto_button.setGeometry(QtCore.QRect(153, 140, 105, 30))
        self.dialog_hand_auto_auto_button.setStyleSheet(".QPushButton {\n"
"    background-color:  #393E46;\n"
"    color: #EEEEEE;\n"
"    font-size: 12px;\n"
"    font-weight: bold;\n"
"    border: 1px solid #393E46;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
".QPushButton:hover {\n"
"    background-color: #00ADB5;\n"
"    border-color:  #00ADB5;\n"
"}\n"
"\n"
".QPushButton:pressed {\n"
"    background-color: #222831;\n"
"}")
        self.dialog_hand_auto_auto_button.setObjectName("dialog_hand_auto_auto_button")
        self.dialog_hand_auto_text_frame = QtWidgets.QFrame(self.dialog_hand_auto_back_frame)
        self.dialog_hand_auto_text_frame.setGeometry(QtCore.QRect(70, 25, 161, 101))
        self.dialog_hand_auto_text_frame.setStyleSheet(".QFrame {\n"
"    border: 1px solid #c2ebec;\n"
"    border-radius: 6px;\n"
"    background-color: #c2ebec;\n"
"}")
        self.dialog_hand_auto_text_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.dialog_hand_auto_text_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.dialog_hand_auto_text_frame.setObjectName("dialog_hand_auto_text_frame")
        self.dialog_hand_auto_frame_label = QtWidgets.QLabel(self.dialog_hand_auto_text_frame)
        self.dialog_hand_auto_frame_label.setGeometry(QtCore.QRect(5, 5, 151, 91))
        self.dialog_hand_auto_frame_label.setStyleSheet(".QLabel {\n"
"    border: 2px dashed #393E46;\n"
"    border-radius: 5px;\n"
"    padding: 40px;\n"
"}")
        self.dialog_hand_auto_frame_label.setText("")
        self.dialog_hand_auto_frame_label.setObjectName("dialog_hand_auto_frame_label")
        self.dialog_hand_auto_text_label = QtWidgets.QLabel(self.dialog_hand_auto_text_frame)
        self.dialog_hand_auto_text_label.setGeometry(QtCore.QRect(30, 10, 111, 80))
        self.dialog_hand_auto_text_label.setStyleSheet(".QLabel {\n"
"    font-size: 10px;\n"
"    font-weight: bold;\n"
"    text-align: center;\n"
"    color: #222831\n"
"}")
        self.dialog_hand_auto_text_label.setObjectName("dialog_hand_auto_text_label")

        self.retranslateUi(dialog_hand_auto)
        QtCore.QMetaObject.connectSlotsByName(dialog_hand_auto)

    def retranslateUi(self, dialog_hand_auto):
        _translate = QtCore.QCoreApplication.translate
        dialog_hand_auto.setWindowTitle(_translate("dialog_hand_auto", "Dialog"))
        self.dialog_hand_auto_manual_button.setText(_translate("dialog_hand_auto", "manual"))
        self.dialog_hand_auto_auto_button.setText(_translate("dialog_hand_auto", "face id"))
        self.dialog_hand_auto_text_label.setText(_translate("dialog_hand_auto", "<html><head/><body><p><span style=\" font-size:10pt;\">Choose how you</span><br/><span style=\" font-size:10pt;\">want to do it</span><br/><span style=\" font-size:12pt;\">.........|............</span><br/><span style=\" font-size:12pt;\">........\\/..........</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialog_hand_auto = QtWidgets.QDialog()
    ui = Ui_dialog_hand_auto()
    ui.setupUi(dialog_hand_auto)
    dialog_hand_auto.show()
    sys.exit(app.exec_())
