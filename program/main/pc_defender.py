import sys
import os
import cv2 as cv
import numpy as np
import shutil
import logging
from os import environ
import datetime

from tools.files_hashing_instruments import hash_module
from tools import thread, timer

from gui.setting.json_setting import js_setting
from gui import ui_design, ui_check_user_dialog, ui_manual_auto_dialog, ui_user_result_dialog, qt_extended_widgets
from gui import resource

from PyQt5.QtWidgets import QApplication, QPushButton, QFileDialog, QLineEdit, QMainWindow
from PyQt5 import QtCore
from PyQt5.QtCore import Qt, QTimer, pyqtSignal, QEvent
from PyQt5.QtGui import QPixmap, QImage


os.chdir(os.path.dirname(os.path.realpath(__file__)))
SETTING_FILE_PATH = r'.\gui\setting\setting.json'
FILE_HASHING_PATH = r'..\data\hash_codes'
NET_WEIGHT = r'..\data\face_id_data\net_weight\net_model.pth'

def suppress_qt_warnings():
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"

class MainWindow(QMainWindow):

    signal_face_image_saving_end = pyqtSignal()
    signal_face_in_camera_set_extension_button_state = pyqtSignal()

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = ui_design.Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFocus()

        self.logging_adjust()
        self.main_logger = logging.getLogger()
        self.main_logger.info(f'Program starts at time-({datetime.datetime.now()}).')

        app.focusChanged.connect(self.main_window_focus_changed)

        self.program_active = False
        self.camera_connected = False
        self.camera_work = False
        self.blocked_add_upgrade_reset_button_for_all = False
        self.encrypting_state = None
        self.face_id_registered = False
        self.face_id_training = False
        self.upgrade_face_training = False
        self.main_status_label_in_work = False
        self.face_img_now = None
        self.saving_face_img = False
        self.stop_show_img = False
        self.password = None
        self.page_now = None

        self.previous_status = []         
        self.status = []
        self.saved_face_image_list = []
        self.files_list = []
        self.dir_list = []
        self.not_decrypted_file = []

        self.max_saved_face_img_number = 100

        self.time_main_status_reset = 1000
        self.time_main_ui_interface_reset = 5000
        self.time_to_start_saving_face = 4000
        self.time_to_reset_saved_face_list = 10000
        self.time_to_connect_to_camera = 6000

        self.main_status_reset_timer = QTimer()
        self.main_status_reset_timer.setInterval(self.time_main_status_reset)
        self.main_status_reset_timer.timeout.connect(self.reset_main_status)
        self.main_status_reset_timer.start()

        self.page_main_interface_reset_timer = QTimer()
        self.page_main_interface_reset_timer.setInterval(self.time_main_ui_interface_reset)
        self.page_main_interface_reset_timer.timeout.connect(self.reset_page_main_interface)

        self.page_extension_interface_reset_timer = QTimer()
        self.page_extension_interface_reset_timer.setInterval(self.time_main_ui_interface_reset)
        self.page_extension_interface_reset_timer.timeout.connect(self.reset_page_extension_interface)

        self.page_setting_interface_reset_timer = QTimer()
        self.page_setting_interface_reset_timer.setInterval(self.time_main_ui_interface_reset)
        self.page_setting_interface_reset_timer.timeout.connect(self.reset_page_setting_interface)

        self.timer_to_start_saving_faces = QTimer()
        self.timer_to_start_saving_faces.setInterval(self.time_to_start_saving_face)
        self.timer_to_start_saving_faces.setSingleShot(True)
        self.timer_to_start_saving_faces.timeout.connect(self.start_save_face_process)

        self.timer_to_connect_to_camera = QTimer()
        self.timer_to_connect_to_camera.setInterval(self.time_to_connect_to_camera)
        self.timer_to_connect_to_camera.setSingleShot(True)
        self.timer_to_connect_to_camera.timeout.connect(self.cant_connect_to_camera_method)

        self.timer_no_face_in_camera = QTimer()
        self.timer_no_face_in_camera.setInterval(self.time_to_reset_saved_face_list)
        self.timer_no_face_in_camera.setSingleShot(True)
        self.timer_no_face_in_camera.timeout.connect(self.reset_saved_face_list_end_operation)

        self.signal_face_image_saving_end.connect(self.start_face_id_training_process)
        self.signal_face_in_camera_set_extension_button_state.connect(self.set_button_extension_state_method)

        self.setting = js_setting(SETTING_FILE_PATH)

        self.hashing = hash_module.Hash_files(FILE_HASHING_PATH)

        self._translate = QtCore.QCoreApplication.translate

        self.dialog_user_check = qt_extended_widgets.ChildDialog()
        self.ui_user_check_dialog = ui_check_user_dialog.Ui_Dialog_user_check()
        self.ui_user_check_dialog.setupUi(self.dialog_user_check)

        self.ui_user_check_dialog.page_password_check_see_password_checkbox.stateChanged.connect(self.see_dialog_password_place)
        self.ui_user_check_dialog.page_password_check_cancel_button.clicked.connect(lambda: self.close_dialog_window(self.dialog_user_check))
        self.ui_user_check_dialog.page_password_check_submit_button.clicked.connect(self.submit_encrypt_decrypt_file)
        self.ui_user_check_dialog.page_face_id_cancel_button.clicked.connect(lambda: self.close_dialog_window(self.dialog_user_check))
        self.ui_user_check_dialog.page_face_id_using_password_button.clicked.connect(self.dialog_user_check_changed_page_to_password)
        self.dialog_user_check.window_closing.connect(lambda: self.close_dialog_window(self.dialog_user_check))

        self.dialog_checked_result = qt_extended_widgets.ChildDialog()
        self.ui_checked_result_dialog = ui_user_result_dialog.Ui_Dialog_user_result()
        self.ui_checked_result_dialog.setupUi(self.dialog_checked_result)

        self.ui_checked_result_dialog.dialog_user_result_ok_button.clicked.connect(self.close_dialog_checked_result)

        self.dialog_hand_auto = qt_extended_widgets.ChildDialog()
        self.ui_manual_auto_dialog = ui_manual_auto_dialog.Ui_dialog_hand_auto()
        self.ui_manual_auto_dialog.setupUi(self.dialog_hand_auto)

        self.dialog_hand_auto.window_closing.connect(lambda: self.close_dialog_window(self.dialog_user_check))
        self.ui_manual_auto_dialog.dialog_hand_auto_manual_button.clicked.connect(self.manual_mode)
        self.ui_manual_auto_dialog.dialog_hand_auto_auto_button.clicked.connect(self.face_id_auto_mode)

        self.ui.home_button.clicked.connect(lambda: self.change_curent_page(self.ui.page_home))
        self.ui.setting_button.clicked.connect(lambda: self.change_curent_page(self.ui.page_setting))
        self.ui.extension_button.clicked.connect(lambda: self.change_curent_page(self.ui.page_extension))
        self.ui.news_button.clicked.connect(lambda: self.change_curent_page(self.ui.page_news))
        self.ui.info_button.clicked.connect(lambda: self.change_curent_page(self.ui.page_info))

        self.ui.page_setting_submit_button.clicked.connect(self.submit_setting)

        self.ui.page_home_reset_files_button.clicked.connect(lambda: self.reset_list_widget(self.ui.drag_files_main_list_widget))
        self.ui.page_home_reset_folder_button.clicked.connect(lambda: self.reset_list_widget(self.ui.drag_folder_main_list_widget))
        self.ui.drag_files_main_browse_button.clicked.connect(self.get_file_names)
        self.ui.drag_folder_main_browse_button.clicked.connect(self.get_folder_name)

        self.ui.page_extension_see_password_checkbox.stateChanged.connect(self.see_password_place)
        self.ui.page_extension_add_button.clicked.connect(self.add_new_face_id)
        self.ui.page_extension_upgrade_button.clicked.connect(self.upgrade_face_id)
        self.ui.page_extension_reset_button.clicked.connect(self.reset_user)
        self.ui.page_extension_enter_password_line_edit.focus_in_signal.connect(self.password_ented_line_edit_focused)
        self.ui.page_extension_enter_password_line_edit.focus_out_signal.connect(self.password_ented_line_edit_unfocused)

        self.ui.page_home_encypt_button.clicked.connect(self.encrypt_files)
        self.ui.page_home_decrypt_button.clicked.connect(self.decrypt_files)

        self.thread_get_video_image = thread.thread_get_image_camera()
        self.thread_get_video_image.cant_connect_to_camera.connect(self.cant_connect_to_camera_method)
        self.thread_get_video_image.cant_get_img.connect(self.cant_get_img_method)
        self.thread_get_video_image.camera_work_good.connect(self.camera_work_good_method)
        self.thread_get_video_image.get_img_without_circled_face.connect(self.show_img_without_circled_face)
        self.thread_get_video_image.get_img_with_circled_face.connect(self.show_img_with_circled_face)
        self.thread_get_video_image.get_only_face_img.connect(self.get_only_face_img_method)
        self.thread_get_video_image.there_is_no_face.connect(self.there_is_no_face_method)

        self.main_logger.info('All main variables registered.')

        self.set_start_program_state()

    def main_window_focus_changed(self):
        if self.isActiveWindow() and not self.program_active:
            print('window active')
            self.get_out_sleep_mode()
            self.program_active = True
        elif not self.isActiveWindow() and self.program_active:
            print('window not active')
            self.get_in_sleep_mode()
            self.program_active = False

    def get_out_sleep_mode(self):
        print('get out of sleep mode')
        if self.page_now == 'page_extension':
            self.thread_get_video_image.start()
            self.ui.page_extension_camera_view_image_label.setPixmap(QPixmap(':/icons/icons/icons8-picture-384.png'))
            self.ui.page_extension_camera_view_image_label.setScaledContents(True)
            self.ui.page_extension_camera_view_text_label.setText('Connecting to the camera...')
            self.ui.page_extension_camera_view_side_text_label.setText('<- No image')
            self.enable_button(False, self.ui.page_extension_add_button, self.ui.page_extension_upgrade_button, self.ui.page_extension_reset_button)
            self.restart_qtimer(self.timer_to_connect_to_camera)

    def get_in_sleep_mode(self):
        print('get in sleep mode')
        if self.timer_to_connect_to_camera.isActive():
            self.timer_to_connect_to_camera.stop()

        if self.page_extension_interface_reset_timer.isActive():
            self.page_extension_interface_reset_timer.stop()
            
        if self.thread_get_video_image.isRunning():
            self.thread_get_video_image.stop()

    def changeEvent(self, event):
        if event.type() == QEvent.WindowStateChange:
            if self.windowState() & Qt.WindowMinimized:
                self.get_in_sleep_mode()
                self.program_active = False

    def reset_page_main_interface(self):
        self.ui.drag_files_side_label.setText('<- Choose files that\n     you want to\n     encrypt or decrypt.')
        self.ui.drag_folder_side_label.setText('<- Choose place or\n     folder where you\n     want to put\n     your files.')

    def reset_page_extension_interface(self):
        self.ui.page_extension_enter_password_side_text_label.setText("<- Enter password")
        self.ui.page_extension_enter_password_side_text_label.setFixedHeight(15)
        self.ui.page_extension_see_password_checkbox.setChecked(False)
        
        if self.face_id_registered:
            self.ui.page_extension_registered_users_text_label.setText('Face id registered :)')
            self.ui.page_extension_add_button.setEnabled(False)
            self.enable_button(True, self.ui.page_extension_upgrade_button, self.ui.page_extension_reset_button)
        elif self.face_id_training:
            self.ui.page_extension_registered_users_text_label.setText('Face id training now ...')
            self.enable_button(False, self.ui.page_extension_add_button, self.ui.page_extension_upgrade_button, self.ui.page_extension_reset_button)
        else:
            self.ui.page_extension_registered_users_text_label.setText('User not registered now :(')
            self.ui.page_extension_add_button.setEnabled(True)
            self.enable_button(False, self.ui.page_extension_upgrade_button, self.ui.page_extension_reset_button)

        if not self.camera_work:
            self.enable_button(False, self.ui.page_extension_upgrade_button, self.ui.page_extension_add_button)
            self.ui.page_extension_camera_view_image_label.setPixmap(QPixmap(':/icons/icons/icons8-picture-384.png'))
            self.ui.page_extension_camera_view_text_label.setText("Can't connect to camera :(")

    def reset_page_setting_interface(self):
            self.set_setting()

    def submit_encrypt_decrypt_file(self):
        password = self.ui_user_check_dialog.page_password_check_enter_password_line_edit.text()
        self.ui_user_check_dialog.page_password_check_enter_password_line_edit.setText('')
        if len(password) > 0:
            self.encrypt_decrypt_file_processing(password)
            self.close_dialog_window(self.dialog_user_check)
        else:
            self.ui_user_check_dialog.page_password_check_enter_password_text_label.setText("Password not entered\n   Try again")

    def face_id_processing_end(self, face_password):
        if len(face_password) > 0:
            self.ui_checked_result_dialog.dialog_user_result_information_frame_text_label.setText("All good :)")
            self.ui_checked_result_dialog.dialog_user_result_information_pixmap.setPixmap(QPixmap(':/icons/icons/icons8-checkmark-384.png'))
            self.dialog_checked_result.show()
            self.encrypt_decrypt_file_processing(password=face_password)
        else:
            self.ui_checked_result_dialog.dialog_user_result_information_frame_text_label.setText("Can't recognise you :(")
            self.ui_checked_result_dialog.dialog_user_result_information_pixmap.setPixmap(QPixmap(':/icons/icons/icons8-unavailable-384.png'))
            self.dialog_checked_result.show()

    def check_face_id(self):
        if self.camera_work:
            self.thread_face_id_processing = thread.face_id_processing(self.saved_face_image_list, self.setting)
            self.thread_face_id_processing.face_id_processing_end.connect(self.face_id_processing_end)
            self.thread_face_id_processing.run()
        else:
            self.ui_user_check_dialog.page_face_id_face_animation_text_label.setText('Camera not work :(')

    def encrypt_decrypt_file_processing(self, password=None):
        pass_bytes = bytes(password, "UTF-8")
        if self.encrypting_state:
                self.thread_encrypt_decrypt_files = thread.encrypt_decrypt_tread(self.files_list, self.dir_list[0], encrypt=True, password_bytes=pass_bytes, file_hashing_path=FILE_HASHING_PATH)
        else:
                self.thread_encrypt_decrypt_files = thread.encrypt_decrypt_tread(self.files_list, self.dir_list[0], encrypt=False, password_bytes=pass_bytes, file_hashing_path=FILE_HASHING_PATH)
        self.thread_encrypt_decrypt_files.decryption_invalid_pass.connect(self.invalid_entered_pass)
        self.thread_encrypt_decrypt_files.encrypt_decrypt_in_process.connect(self.show_encrypt_progress)
        self.thread_encrypt_decrypt_files.encrypt_decrypt_ended.connect(self.encrypt_ended)
        self.thread_encrypt_decrypt_files.start()

    def show_encrypt_progress(self, progress):
        process = None
        if self.encrypting_state:
            process = 'Encrypting'
        else:
            process = 'Decrypting'
        self.status.append(f'|{process} progress-{progress}%|')
        self.update_status()

    def encrypt_ended(self):
        if len(self.not_decrypted_file) > 0:
            self.ui_checked_result_dialog.dialog_user_result_information_pixmap.setPixmap(QPixmap(':/icons/icons/icons8-unavailable-384.png'))
            self.ui_checked_result_dialog.dialog_user_result_information_frame_text_label.setText(f'Invalid pass for file with name\n"{os.path.basename(self.not_decrypted_file.pop(0))[:30]}"')
            self.dialog_checked_result.show()
        else:
            self.ui_checked_result_dialog.dialog_user_result_information_pixmap.setPixmap(QPixmap(':/icons/icons/icons8-checkmark-384.png'))
            self.ui_checked_result_dialog.dialog_user_result_information_frame_text_label.setText(f'All good :)')
            self.dialog_checked_result.show()
        self.encrypting_state = None
        self.main_status_label_in_work = False

    def invalid_entered_pass(self, file_path):
        self.not_decrypted_file.append(file_path)

    def close_dialog_checked_result(self):
        self.dialog_checked_result.close()
        if len(self.not_decrypted_file) > 0:
            self.encrypt_ended()

    def reset_main_status(self):
        if not self.main_status_label_in_work:
            if not self.face_id_registered:
                self.status.append('| No users registered |')
                self.update_status()
            else:
                self.status.append('| All good, enjoing :)|')

    def see_dialog_password_place(self):
        if self.ui_user_check_dialog.page_password_check_see_password_checkbox.isChecked():
            self.ui_user_check_dialog.page_password_check_enter_password_line_edit.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.ui_user_check_dialog.page_password_check_enter_password_line_edit.setEchoMode(QLineEdit.EchoMode.Password)

    def prepared_for_encrypt_decrypt(self):
        self.main_logger.info('Start encoding filed.')
        original_files_path = self.get_all_list_widget_items(self.ui.drag_files_main_list_widget)
        destination_folder_path = self.get_all_list_widget_items(self.ui.drag_folder_main_list_widget)

        if len(original_files_path) == 0:
            self.ui.drag_files_side_label.setText('<- There is no files\n   please choose files\n   to encode, decode')
            self.restart_qtimer(self.page_main_interface_reset_timer)
            return 0
        elif len(destination_folder_path) == 0:
            self.ui.drag_folder_side_label.setText('<- There is no folder\n  please choose folder\n   for your files')
            self.restart_qtimer(self.page_main_interface_reset_timer)
            return 0
        else:
            self.files_list = []
            self.dir_list = [] 

            for file_path in original_files_path:
                if os.path.isfile(file_path):
                    self.files_list.append(file_path)
            for folder in destination_folder_path:
                if os.path.isdir(folder):
                    self.dir_list.append(folder)

            if len(self.files_list) == 0:
                self.ui.drag_files_side_label.setText('<- There is no file\n   please choose files\n   to encode, decode')
                self.restart_qtimer(self.page_main_interface_reset_timer)
                return 0
            elif len(self.dir_list) == 0:
                self.ui.drag_folder_side_label.setText('<- There is no folder\n   please choose folder\n   for your files')
                self.restart_qtimer(self.page_main_interface_reset_timer)
                return 0
            else:
                files_size = 0
                
                self.reset_list_widget(self.ui.drag_files_main_list_widget)
                self.reset_list_widget(self.ui.drag_folder_main_list_widget)

                for file in self.files_list:
                    files_size += os.path.getsize(file)
                for dir in self.dir_list:
                    dir_free_space = shutil.disk_usage(dir)

                    if dir_free_space[2] > files_size:
                        if self.face_id_registered:
                            if self.setting.page_setting_auto_face_id_always_checkbox:
                                self.ui_user_check_dialog.dialog_user_check_page.setCurrentWidget(self.ui_user_check_dialog.page_face_id)
                                self.show_dialog_window(self.dialog_user_check)
                                self.check_face_id()
                            else:
                                self.show_dialog_window(self.dialog_hand_auto)
                        else:
                            self.ui_user_check_dialog.dialog_user_check_page.setCurrentWidget(self.ui_user_check_dialog.page_password_check)
                            self.show_dialog_window(self.dialog_user_check)
                        break
                    else:
                        self.dir_list.remove(dir)

                if len(self.dir_list) == 0:
                    self.ui.drag_folder_side_label.setText('<- There is not\n   enough free space')
                    self.restart_qtimer(self.page_main_interface_reset_timer)
                    return 0
        return 1

    def encrypt_files(self):
        self.set_encrypt_state()
        self.prepared_for_encrypt_decrypt()

    def decrypt_files(self):
        self.set_decrypt_state()
        self.prepared_for_encrypt_decrypt()

    def set_encrypt_state(self):
        self.encrypting_state = True

    def set_decrypt_state(self):
        self.encrypting_state = False

    def manual_mode(self):
        self.close_dialog_window(self.dialog_hand_auto)
        self.ui_user_check_dialog.dialog_user_check_page.setCurrentWidget(self.ui_user_check_dialog.page_password_check)
        self.show_dialog_window(self.dialog_user_check)

    def face_id_auto_mode(self):
        self.close_dialog_window(self.dialog_hand_auto)
        self.ui_user_check_dialog.dialog_user_check_page.setCurrentWidget(self.ui_user_check_dialog.page_face_id)
        # self.show_dialog_window(self.dialog_user_check)
        self.check_face_id()

    def show_dialog_window(self, window_obj):
        window_obj.show()
        self.ui.page_home_encypt_button.setEnabled(False)
        self.ui.page_home_decrypt_button.setEnabled(False)
        self.ui.page_home_reset_folder_button.setEnabled(False)
        self.ui.page_home_reset_files_button.setEnabled(False)
        self.ui.drag_files_main_browse_button.setEnabled(False)
        self.ui.drag_folder_main_browse_button.setEnabled(False)

    def close_dialog_window(self, window_obj):
        window_name = window_obj.objectName()
        window_obj.close()
        self.ui.page_home_encypt_button.setEnabled(True)
        self.ui.page_home_decrypt_button.setEnabled(True)
        self.ui.page_home_reset_folder_button.setEnabled(True)
        self.ui.page_home_reset_files_button.setEnabled(True)
        self.ui.drag_files_main_browse_button.setEnabled(True)
        self.ui.drag_folder_main_browse_button.setEnabled(True)

        if window_name == 'Dialog_user_check':
            self.ui_user_check_dialog.page_password_check_enter_password_text_label.setText('........./\.........\n..........|..........\nEnter password')
            self.ui_user_check_dialog.page_password_check_enter_password_line_edit.setText('')
            self.ui_user_check_dialog.page_password_check_see_password_checkbox.setChecked(False)
        elif window_name == 'Dialog_user_result':
            self.ui_checked_result_dialog.dialog_user_result_information_frame_text_label.setText('')
            self.ui_checked_result_dialog.dialog_user_result_information_pixmap.setPixmap(QPixmap(''))
        elif window_name == 'dialog_hand_auto':
            self.ui_manual_auto_dialog.dialog_hand_auto_text_label.setText(self._translate("dialog_hand_auto", "<html><head/><body><p><span style=\" font-size:10pt;\">Choose how you</span><br/><span style=\" font-size:10pt;\">want to do it</span><br/><span style=\" font-size:12pt;\">.........|............</span><br/><span style=\" font-size:12pt;\">........\\/..........</span></p></body></html>"))

    def get_all_list_widget_items(self, list_widget_object):
        items = []
        for index in range(list_widget_object.count()):
            items.append(list_widget_object.item(index).text())
        return items

    def set_start_program_state(self):
        self.main_logger.info('Start getting setting and change main program states.')

        self.ui.main_pages_widget.setCurrentWidget(self.ui.page_home)
        self.setting.get_setting()
        self.set_setting()
        self.face_id_registered = self.setting.face_id_registered
        
        if self.face_id_registered:
            self.status.append('| All good, enjoing :)|')
            self.update_status()
            self.ui.page_extension_registered_users_text_label.setText('Face id registered :)')
        else:
            self.status.append('| No users registered |')
            self.update_status()
            self.ui.page_extension_registered_users_text_label.setText('User not registered now :(')
        
        self.main_logger.info('Start program states setted.')

    def update_status(self):
        if len(self.status) != 0:
            self.previous_status.append(self.ui.main_status_label.text())
            new_state = self.status.pop(0)
            self.ui.main_status_label.setText(new_state)

            self.main_logger.debug('Main program status update to "%s".', new_state)

    def face_id_add_training_end(self):
        self.face_id_registered = True
        self.face_id_training = False
        self.enable_button(True, self.ui.page_extension_reset_button, self.ui.page_extension_upgrade_button)
        self.saved_face_image_list.clear()
        self.restart_qtimer(self.page_extension_interface_reset_timer)
        self.setting.set_face_id_status(True)
        self.main_status_label_in_work = False
        self.ui.page_extension_registered_users_text_label.setText('Face id registered :)')

        self.main_logger.debug('New face id registering ended.')

    def password_ented_line_edit_focused(self):
        self.restart_qtimer(self.page_extension_interface_reset_timer)
        self.ui.page_extension_enter_password_side_text_label.setText("<- At least 12 symbols\n     recomended")
        self.ui.page_extension_enter_password_side_text_label.setFixedHeight(32)

    def password_ented_line_edit_unfocused(self):
        self.ui.page_extension_enter_password_side_text_label.setText("<- Enter password")
        self.ui.page_extension_enter_password_side_text_label.setFixedHeight(15)

    def reset_user(self):
        self.password = self.ui.page_extension_enter_password_line_edit.text()
        self.ui.page_extension_enter_password_line_edit.setText('')
        if len(self.password) != 0:
            saved_password = self.hashing.get_user_pass('client')
            password_byte = bytes(self.password, "UTF-8")
            hashed_entered_password = self.hashing.string_hashing(password_byte)
            if saved_password == hashed_entered_password:
                self.ui.page_extension_enter_password_side_text_label.setText("<- successful :)")
                self.ui.page_extension_enter_password_side_text_label.setFixedHeight(15)
                if os.path.exists(FILE_HASHING_PATH):
                    shutil.rmtree(FILE_HASHING_PATH)
                os.mkdir(FILE_HASHING_PATH)
                if os.path.exists(NET_WEIGHT):
                    os.remove(NET_WEIGHT)
                self.face_id_registered = False
                self.setting.set_face_id_status(False)
                self.ui.page_extension_add_button.setEnabled(True)
                self.enable_button(False, self.ui.page_extension_upgrade_button, self.ui.page_extension_reset_button)
                self.ui.page_extension_registered_users_text_label.setText('User not registered now')
                self.main_logger.debug('Password right, user face id reseted.')
            else:
                self.ui.page_extension_enter_password_side_text_label.setText("<- Incorrect :(")
                self.ui.page_extension_enter_password_side_text_label.setFixedHeight(15)
                self.main_logger.debug('User face id password entered incorrect.')
        else:
            self.ui.page_extension_enter_password_side_text_label.setText("<- Password\n    not entered")
            self.ui.page_extension_enter_password_side_text_label.setFixedHeight(32)
            self.main_logger.debug('User not enter password at all.')

    def upgrade_face_id(self):
        self.password = self.ui.page_extension_enter_password_line_edit.text()
        self.ui.page_extension_enter_password_line_edit.setText('')
        self.main_logger.info('User press "add" button')
        if len(self.password) > 0:

            saved_password = self.hashing.get_user_pass('client')
            password_byte = bytes(self.password, "UTF-8")
            hashed_entered_password = self.hashing.string_hashing(password_byte)
            if saved_password == hashed_entered_password:

                self.timer_to_start_saving_faces.start()
                self.stop_show_img = True
                self.upgrade_face_training = True
                self.face_id_registered = False
                self.face_id_training = True
                self.main_status_label_in_work = True
                self.enable_button(False, self.ui.page_extension_add_button, self.ui.page_extension_upgrade_button, self.ui.page_extension_reset_button)

                self.ui.page_extension_camera_view_image_label.setScaledContents(True)
                self.ui.page_extension_camera_view_image_label.setPixmap(QPixmap(':/icons/icons/icons8-iron-man-material-outlined/icons8-iron-man-384.png'))
                self.ui.page_extension_camera_view_side_text_label.setText('<- ...')
                self.ui.page_extension_registered_users_text_label.setText('Looking on camera when scanning starts')
                self.ui.page_extension_enter_password_side_text_label.setText("<- successful :)")
                self.ui.page_extension_enter_password_side_text_label.setFixedHeight(15)
                self.restart_qtimer(self.page_extension_interface_reset_timer)
            else:
                self.ui.page_extension_enter_password_side_text_label.setText("<- Incorrect :(")
                self.ui.page_extension_enter_password_side_text_label.setFixedHeight(15)
                self.main_logger.debug('User enter incorrect password.')
        else:
            self.ui.page_extension_enter_password_side_text_label.setText("<- Password\n    not entered")
            self.ui.page_extension_enter_password_side_text_label.setFixedHeight(32)
            self.restart_qtimer(self.page_extension_interface_reset_timer)
            self.main_logger.debug('User not enter password.')

    def reset_saved_face_list_end_operation(self):
        self.saved_face_image_list.clear()
        self.saving_face_img = False
        self.password = None
        self.main_status_label_in_work = False
        self.face_id_training = False
        self.ui.page_extension_registered_users_text_label.setText('Sorry we can`t add your face id :(')
        self.restart_qtimer(self.page_extension_interface_reset_timer)

    def start_face_id_training_process(self):
        self.saving_face_img = False
        self.ui.page_extension_registered_users_text_label.setText('Scan succesfuly, now traninig begins :)')
        self.restart_qtimer(self.page_extension_interface_reset_timer)

        if self.upgrade_face_training:
            # with open(os.path.join(FILE_HASHING_PATH, 'face_id.txt'), 'w') as face_file:
            #     face_file.write(self.password)

            password_byte = bytes(self.password, "UTF-8")
            self.hashing.add_new_pass_salt_to_hash("client", password_byte)

            print(self.saved_face_image_list)
            self.thread_upgrade_user = thread.add_upgrade_user(self.saved_face_image_list, self.ui.main_status_label, self.setting, True, password=self.password)
            self.thread_upgrade_user.end_training_face_id.connect(self.face_id_add_training_end)
            self.thread_upgrade_user.start()
            self.enable_button(False, self.ui.page_extension_add_button, self.ui.page_extension_reset_button, self.ui.page_extension_upgrade_button)
            self.password = None
            self.main_logger.debug('User enter correct password, face id upgrade thread starts.')
        else:
            # with open(os.path.join(FILE_HASHING_PATH, 'face_id.txt'), 'w') as face_file:
            #     face_file.write(self.password)

            password_byte = bytes(self.password, "UTF-8")
            self.hashing.add_new_pass_salt_to_hash("client", password_byte)

            print(self.saved_face_image_list)
            self.thread_add_user = thread.add_upgrade_user(self.saved_face_image_list, self.ui.main_status_label, self.setting, False, password=self.password)
            self.thread_add_user.end_training_face_id.connect(self.face_id_add_training_end)
            self.thread_add_user.start()
            self.enable_button(False, self.ui.page_extension_add_button, self.ui.page_extension_reset_button, self.ui.page_extension_upgrade_button)
            self.password = None
            self.main_logger.debug('User enter password and start thread function to add new face id.')

    def start_save_face_process(self):
        self.saved_face_image_list = []
        self.saving_face_img = True
        self.page_extension_interface_reset_timer.stop()
        self.stop_show_img = False
        self.ui.page_extension_registered_users_text_label.setText('Now scanning you ...')

    def add_new_face_id(self):
        self.password = self.ui.page_extension_enter_password_line_edit.text()
        self.ui.page_extension_enter_password_line_edit.setText('')
        self.main_logger.info('User press "add" button')
        if len(self.password) > 0:

            self.timer_to_start_saving_faces.start()
            self.stop_show_img = True
            self.face_id_registered = False
            self.face_id_training = True
            self.main_status_label_in_work = True
            self.upgrade_face_training = False
            self.enable_button(False, self.ui.page_extension_add_button, self.ui.page_extension_upgrade_button, self.ui.page_extension_reset_button)

            self.ui.page_extension_camera_view_image_label.setScaledContents(True)
            self.ui.page_extension_camera_view_image_label.setPixmap(QPixmap(':/icons/icons/icons8-iron-man-material-outlined/icons8-iron-man-384.png'))
            self.ui.page_extension_camera_view_side_text_label.setText('<- ...')
            self.ui.page_extension_enter_password_side_text_label.setText("<- successful :)")
            self.ui.page_extension_enter_password_side_text_label.setFixedHeight(15)
            self.ui.page_extension_registered_users_text_label.setText('Looking on camera when scanning starts')
            self.restart_qtimer(self.page_extension_interface_reset_timer)
        else:
            self.ui.page_extension_enter_password_side_text_label.setText("<- Password\n    not entered")
            self.ui.page_extension_enter_password_side_text_label.setFixedHeight(32)
            self.restart_qtimer(self.page_extension_interface_reset_timer)
            self.main_logger.debug('User not enter password but want to add new face id.')

    def enable_button(self, enable:bool, *args, blocked_add_upgrade_reset_button_for_all=None):
        if enable:
            for arg in args:
                arg.setEnabled(True)
                self.main_logger.debug('Button "%s" unblocked.', arg)
        else:
            for arg in args:
                arg.setEnabled(False)
                self.main_logger.debug('Button "%s" blocked.', arg)

        if type(blocked_add_upgrade_reset_button_for_all) == bool:
            self.blocked_add_upgrade_reset_button_for_all = blocked_add_upgrade_reset_button_for_all
            self.main_logger.debug('Variable "blocked_add_upgrade_reset_button_for_all" get value "%s".', blocked_add_upgrade_reset_button_for_all)

    def set_button_extension_state_method(self):
        if not self.face_id_training:
            if self.face_id_registered:
                self.enable_button(False, self.ui.page_extension_add_button)
                self.enable_button(True, self.ui.page_extension_reset_button, self.ui.page_extension_upgrade_button)
            else:
                self.enable_button(True, self.ui.page_extension_add_button)
                self.enable_button(False, self.ui.page_extension_reset_button, self.ui.page_extension_upgrade_button)
                
    def convert_img_from_cv_to_qt(self, img:np.ndarray):
        frame_flip = cv.flip(img, 1)
        image_qt_format = QImage(frame_flip.data, frame_flip.shape[1], frame_flip.shape[0],
                                frame_flip.strides[0], QImage.Format_RGB888)
        return image_qt_format

    def cant_get_img_method(self):
        self.ui.page_extension_camera_view_text_label.setText("Can't get image from camera :(")
        self.restart_qtimer(self.page_extension_interface_reset_timer)
        self.ui.page_extension_camera_view_image_label.setPixmap(QPixmap(':/icons/icons/icons8-unavailable-384.png'))
        self.ui.page_extension_camera_view_image_label.setScaledContents(True)
        self.camera_connected = True
        self.camera_work = False

    def cant_connect_to_camera_method(self):
        self.ui.page_extension_camera_view_text_label.setText("Can't connect to camera :(")
        self.restart_qtimer(self.page_extension_interface_reset_timer)
        self.ui.page_extension_camera_view_image_label.setScaledContents(True)
        self.ui.page_extension_camera_view_image_label.setPixmap(QPixmap(':/icons/icons/icons8-unavailable-384.png'))
        self.camera_connected = False
        self.camera_work = False

    def camera_work_good_method(self):
        self.camera_connected = True
        self.camera_work = True
        self.ui.page_extension_camera_view_text_label.setText('')
        self.timer_to_connect_to_camera.stop()
        self.restart_qtimer(self.page_extension_interface_reset_timer)

    def there_is_no_face_method(self):
        if not self.stop_show_img:
            self.ui.page_extension_camera_view_side_text_label.setText('<- No Faces')

        self.face_img_now = None

        if self.saving_face_img:
            self.ui.page_extension_camera_view_side_text_label.setText(f'<- make sure that\n    your face in\n    camera view')
            if not self.timer_no_face_in_camera.isActive():
                self.timer_no_face_in_camera.start()

    def get_only_face_img_method(self, img:np.ndarray):
        if not self.stop_show_img:
            self.ui.page_extension_camera_view_side_text_label.setText('<- Your face')

        self.signal_face_in_camera_set_extension_button_state.emit()

        self.face_img_now = img

        if self.saving_face_img:
            saved_face_image_number = len(self.saved_face_image_list)

            if self.timer_no_face_in_camera.isActive():
                self.timer_no_face_in_camera.stop()

            if saved_face_image_number < self.max_saved_face_img_number:
                self.saved_face_image_list.append(self.face_img_now)
                self.ui.page_extension_camera_view_side_text_label.setText(f'<- scanning {int(self.max_saved_face_img_number*saved_face_image_number/100)}%')
            else:
                self.signal_face_image_saving_end.emit()

    def show_img_without_circled_face(self, img:np.ndarray):
        if not self.stop_show_img:
            img_qt = self.convert_img_from_cv_to_qt(img)
            picture = img_qt.scaled(200, 200, Qt.KeepAspectRatio)
            self.ui.page_extension_camera_view_image_label.setScaledContents(False)
            self.ui.page_extension_camera_view_image_label.setPixmap(QPixmap.fromImage(picture))
            self.ui.page_extension_camera_view_text_label.setText('')

    def show_img_with_circled_face(self, img:np.ndarray):
        if not self.stop_show_img:
            img_qt = self.convert_img_from_cv_to_qt(img)
            picture = img_qt.scaled(200, 200, Qt.KeepAspectRatio)
            self.ui.page_extension_camera_view_image_label.setScaledContents(False)
            self.ui.page_extension_camera_view_image_label.setPixmap(QPixmap.fromImage(picture))
            self.ui.page_extension_camera_view_text_label.setText('')

    def see_password_place(self):
        if self.ui.page_extension_see_password_checkbox.isChecked():
            self.ui.page_extension_enter_password_line_edit.setEchoMode(QLineEdit.EchoMode.Normal)
            self.restart_qtimer(self.page_extension_interface_reset_timer)
        else:
            self.ui.page_extension_enter_password_line_edit.setEchoMode(QLineEdit.EchoMode.Password)
            self.restart_qtimer(self.page_extension_interface_reset_timer)

    def get_file_names(self):
        file_links = QFileDialog.getOpenFileNames(self, "Choose Files to modify", r"C:\\")
        self.ui.drag_files_main_list_widget.addItems(file_links[0])

    def get_folder_name(self):
        folder_link = QFileDialog.getExistingDirectory(self, "Choose directory to save", r"C:\\")
        self.ui.drag_folder_main_list_widget.addItem(folder_link)

    def reset_list_widget(self, list_widget: object):
        list_widget.clear()

    def set_setting(self):
        self.ui.page_setting_face_id_complexity_slider.setValue(self.setting.page_setting_face_id_complexity_slider)
        self.ui.page_setting_face_id_training_slider.setValue(self.setting.page_setting_face_id_training_slider)
        self.ui.page_setting_windows_notification_checkbox.setChecked(self.setting.page_setting_windows_notification_checkbox)
        self.ui.page_setting_autostart_checkbox.setChecked(self.setting.page_setting_autostart_checkbox)
        self.ui.page_setting_auto_face_id_always_checkbox.setChecked(self.setting.page_setting_auto_face_id_always_checkbox)
        self.face_id_registered = self.setting.face_id_registered

    def submit_setting(self):
        face_id_complexity = self.ui.page_setting_face_id_complexity_slider.value()
        face_id_training = self.ui.page_setting_face_id_training_slider.value()
        windows_notification = self.ui.page_setting_windows_notification_checkbox.checkState()
        autostart = self.ui.page_setting_autostart_checkbox.checkState()
        auto_face_id = self.ui.page_setting_auto_face_id_always_checkbox.checkState()
        face_id_registered = self.face_id_registered

        self.setting.load_setting(face_id_complexity, face_id_training, windows_notification, autostart, auto_face_id, face_id_registered)

        self.set_setting()

    def restart_qtimer(self, qtimer_obj):
        if qtimer_obj.isActive():
            qtimer_obj.stop()
            qtimer_obj.start()
        else:
            qtimer_obj.start()

    def dialog_user_check_changed_page_to_password(self):
        self.ui_user_check_dialog.dialog_user_check_page.setCurrentWidget(self.ui_user_check_dialog.page_password_check)

    def change_curent_page(self, page: object):
        self.ui.main_pages_widget.setCurrentWidget(page)
        self.change_active_button_style()
        self.page_now = page.objectName()
        self.main_logger.info(f'User changed page on {self.page_now}.')

        if self.page_now == 'page_main':
            self.ui.drag_files_side_label.setText('<- Choose files that\n     you want to\n     encrypt or decrypt.')
            self.ui.drag_folder_side_label.setText('<- Choose place or\n     folder where you\n     want to put\n     your files.')
            if not self.page_main_interface_reset_timer.isActive():
                self.page_main_interface_reset_timer.start()
        else:
            if self.page_main_interface_reset_timer.isActive():
                self.page_main_interface_reset_timer.stop()


        if self.page_now == 'page_extension':
            self.thread_get_video_image.start()
            self.ui.page_extension_camera_view_image_label.setPixmap(QPixmap(':/icons/icons/icons8-picture-384.png'))
            self.ui.page_extension_camera_view_image_label.setScaledContents(True)
            self.ui.page_extension_camera_view_text_label.setText('Connecting to the camera...')
            self.ui.page_extension_camera_view_side_text_label.setText('<- No image')
            self.enable_button(False, self.ui.page_extension_add_button, self.ui.page_extension_upgrade_button, self.ui.page_extension_reset_button)
            self.restart_qtimer(self.timer_to_connect_to_camera)

        else:
            if self.timer_to_connect_to_camera.isActive():
                self.timer_to_connect_to_camera.stop()

            if self.page_extension_interface_reset_timer.isActive():
                self.page_extension_interface_reset_timer.stop()
                
            if self.thread_get_video_image.isRunning():
                self.thread_get_video_image.stop()
        
        if self.page_now == 'page_setting':
            if self.page_setting_interface_reset_timer.isActive():
                self.page_setting_interface_reset_timer.stop()
        else:
            self.restart_qtimer(self.page_setting_interface_reset_timer)

    def change_active_button_style(self):
            for side_button in self.ui.side_frame.findChildren(QPushButton):
                if side_button.objectName() != self.sender().objectName():
                    default_style = side_button.styleSheet().replace(".QPushButton {\n"
                                                                        "    padding: 3px;\n"
                                                                        "    padding-top: 5px;\n"
                                                                        "    padding-bottom: 5px;\n"
                                                                        "    margin: 5px;\n"
                                                                        "    background-color: #222831;\n"
                                                                        "    border-width: 2px;\n"
                                                                        "     border-style: solid;\n"
                                                                        "    border-color: #E3E3E3;\n"
                                                                        "    border-radius: 12px;\n"
                                                                        "}\n", ".QPushButton {\n"
                                                                        "    padding: 3px;\n"
                                                                        "    padding-top: 5px;\n"
                                                                        "    padding-bottom: 5px;\n"
                                                                        "    margin: 5px;\n"
                                                                        "    background-color: rgba(255, 255, 255, 0);\n"
                                                                        "    border-width: 2px;\n"
                                                                        "     border-style: solid;\n"
                                                                        "    border-color: #E3E3E3;\n"
                                                                        "    border-radius: 12px;\n"
                                                                        "}\n")
                                                                        
                    side_button.setStyleSheet(default_style)
            new_style = self.sender().styleSheet().replace(".QPushButton {\n"
                                                            "    padding: 3px;\n"
                                                            "    padding-top: 5px;\n"
                                                            "    padding-bottom: 5px;\n"
                                                            "    margin: 5px;\n"
                                                            "    background-color: rgba(255, 255, 255, 0);\n"
                                                            "    border-width: 2px;\n"
                                                            "     border-style: solid;\n"
                                                            "    border-color: #E3E3E3;\n"
                                                            "    border-radius: 12px;\n"
                                                            "}\n", ".QPushButton {\n"
                                                            "    padding: 3px;\n"
                                                            "    padding-top: 5px;\n"
                                                            "    padding-bottom: 5px;\n"
                                                            "    margin: 5px;\n"
                                                            "    background-color: #222831;\n"
                                                            "    border-width: 2px;\n"
                                                            "     border-style: solid;\n"
                                                            "    border-color: #E3E3E3;\n"
                                                            "    border-radius: 12px;\n"
                                                            "}\n")
            self.sender().setStyleSheet(new_style)
        
    def logging_adjust(self, times=1000):
        path = 'logs'

        file_list = os.listdir(path)
        sorted_file_list = []
        for file in file_list:
            text,_ = os.path.splitext(file)
            sorted_file_list.append(int(text))
        sorted_file_list.sort(reverse=True)
        number = len(sorted_file_list)
        if number < times:
            for name in sorted_file_list:
                old_name = str(name) + '.log'
                new_file_name = str(name+1) + '.log'
                os.rename(os.path.join(path, old_name), os.path.join(path, new_file_name))
            
            file_path = os.path.join(path, '0.log')
            logging.basicConfig(filename=file_path, encoding='utf-8', filemode='w', level='DEBUG')
        else:
            for name in sorted_file_list:
                old_name = str(name) + '.log'
                new_file_name = str(name+1) + '.log'
                os.rename(os.path.join(path, old_name), os.path.join(path, new_file_name))
            
            os.remove(os.path.join(path, (str(times)+'.log')))
            file_path = os.path.join(path, '0.log')
            logging.basicConfig(filename=file_path, encoding='utf-8', filemode='w', level='DEBUG')

    def show_window(self):
        self.show()

    def closeEvent(self, event):
        self.dialog_checked_result.close()
        self.dialog_hand_auto.close()
        self.dialog_user_check.close()

if __name__ == "__main__":
    suppress_qt_warnings()
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show_window()
    sys.exit(app.exec_())
