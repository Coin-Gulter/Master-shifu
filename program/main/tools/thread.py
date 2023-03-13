from PyQt5.QtCore import QThread, pyqtSignal, Qt
from PyQt5.QtGui import QImage, QPixmap

import cv2 as cv
import os
import math
import time
import logging
import shutil
import numpy as np
from tools.face_recognition_instruments import face_detection_module, dt_set_module, ai_module
from tools.files_hashing_instruments import hash_module
from tools import timer
from multiprocessing import Process

FACE_JSON_TARGET_PATH = r'..\data\face_id_data\target_json\face_id_target.json'
FACE_DT_PATH = r'..\data\face_id_data\filtered_face_dt'
NET_WEIGHT = r'..\data\face_id_data\net_weight\net_model.pth'
CHARACTERS_NUMBER = 149186

class thread_get_image_camera(QThread):
    get_img_with_circled_face = pyqtSignal(np.ndarray)
    get_img_without_circled_face = pyqtSignal(np.ndarray)
    get_only_face_img = pyqtSignal(np.ndarray)
    there_is_no_face = pyqtSignal()
    camera_work_good = pyqtSignal()
    cant_connect_to_camera = pyqtSignal()
    cant_get_img = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.ThreadActive = True
        self.camera_work_checked_already = False
        self.cant_get_img_checked_already = False
        self.main_logger = logging.getLogger('main_logger')
        self.main_logger.info('Start registering "get camera image thread" main variables.')
        self.main_logger.info('"get camera image thread" main variables registered.')

    def run(self):
        self.main_logger.info('Start "get camera image thread".')
        
        self.ThreadActive = True
        self.camera_work_checked_already = False
        self.cant_get_img_checked_already = False

        Fc_recog = face_detection_module.face_recognition()

        try:
            cap = cv.VideoCapture(0)
        except:
            self.cant_connect_to_camera.emit()
        else:
            while self.ThreadActive:
                bbox = []
                success, img = cap.read()

                if success:
                    if not self.camera_work_checked_already:
                        self.camera_work_good.emit()
                        self.camera_work_checked_already = True
                        self.cant_get_img_checked_already = False
                    img_rgb_not_recognise = cv.cvtColor(img, cv.COLOR_BGR2RGB)
                    img_recog, bbox, detection_score = Fc_recog.faceDetector(img)
                    img_rgb_recognise = cv.cvtColor(img_recog, cv.COLOR_BGR2RGB)

                    if len(bbox) != 0 and detection_score > 0.9:
                        face_image = face_detection_module.cut_face(img_rgb_not_recognise, bbox)
                        face_image = cv.cvtColor(face_image, cv.COLOR_BGR2RGB)
                        self.get_img_with_circled_face.emit(img_rgb_recognise)
                        self.get_only_face_img.emit(face_image)
                    else:
                        self.get_img_without_circled_face.emit(img_rgb_not_recognise)
                        self.there_is_no_face.emit()
                else:
                    if not self.cant_get_img_checked_already:
                        self.cant_get_img.emit()
                        self.camera_work_checked_already = False
                        self.cant_get_img_checked_already = True

            cap.release()

        self.main_logger.debug('"get camera image thread" end working')

    def stop(self):
        self.main_logger.debug('"get camera image thread" stoped working')
        self.ThreadActive = False
        self.quit()

class add_upgrade_user(QThread):
    end_training_face_id = pyqtSignal()

    def __init__(self, faces_list: list, ui_status_label:object, setting:object, upgrade:bool):
        super().__init__()
        self.main_logger = logging.getLogger('main_logger')
        self.main_logger.info('Start registering "add upgrade user thread" main variables.')

        self.upgrade = upgrade        
        self.setting = setting
        self.faces_list = faces_list
        self.ui_status_label = ui_status_label
        self.max_train_iteration = 1000
        self.main_logger.debug('"add upgrade user thread" "upgrade" variable get value - "%s".', self.upgrade)
        self.main_logger.info('"add upgrade user thread" main variables registered.')

    def run(self):
        print(self.faces_list)
        self.main_logger.info('"add upgrade user thread" start working.')

        if not self.upgrade:
            client_path = os.path.join(FACE_DT_PATH,"client")
            if os.path.exists(client_path):
                shutil.rmtree(client_path)
            os.mkdir(client_path)

        model = ai_module.user_detection_net(out_size=2)
        dt_set_module.save_client_face(self.faces_list, folder_path=FACE_DT_PATH)

        dt_set_module.preper_face_id_target_dt_set(FACE_DT_PATH, face_target_path=FACE_JSON_TARGET_PATH)

        iteration = int(self.max_train_iteration*(self.setting.page_setting_face_id_training_slider+1)/100)

        optimizer = ai_module.optim.SGD(model.parameters(), lr=0.0001)
        criterion = ai_module.nn.CrossEntropyLoss()
        training_net = ai_module.net_train(model, optimizer=optimizer, criterion=criterion, pretrained=self.upgrade, face_dt_path=FACE_JSON_TARGET_PATH, path=NET_WEIGHT)
        training_process = Process(target=training_net.train_iter, args=(iteration,))
        training_process.start()

        self.ui_status_label.setText('| face id training ...|')

        training_process.join()
        self.ui_status_label.setText('| FaceId registered :)|')
        self.end_training_face_id.emit()

        self.main_logger.info('"add upgrade user thread" end working')


    def stop(self):
        self.main_logger.debug('"add upgrade user thread"  stoped working')
        self.quit()

class encrypt_decrypt_tread(QThread):

    encrypt_decrypt_in_process = pyqtSignal(int)
    encrypt_decrypt_ended = pyqtSignal()
    decryption_invalid_pass = pyqtSignal(str)

    def __init__(self, files_list, folder, encrypt:bool, password_bytes, file_hashing_path):
        super().__init__()
        self.files_list = files_list
        self.folder = folder
        self.encrypt = encrypt
        self.password_bytes = password_bytes
        self.hashing = hash_module.Hash_files(file_hashing_path)

    def run(self):
        hash_key = self.hashing.password_2_hashkey(self.password_bytes)

        if self.encrypt:
            for index, file_name in enumerate(self.files_list):
                self.hashing.encrypto_file(hash_key, file_name, self.folder)
                self.encrypt_decrypt_in_process.emit(int(index/len(self.files_list)*100))
        else:
            for index, file_name in enumerate(self.files_list):
                if not self.hashing.decrypto_file(hash_key, file_name, self.folder):
                    self.decryption_invalid_pass.emit(file_name)
                self.encrypt_decrypt_in_process.emit(int(index/len(self.files_list)*100))

        self.encrypt_decrypt_ended.emit()

    def stop(self):
        self.quit()

class face_id_processing(QThread):
    face_id_processing_end = pyqtSignal(bool)


    def __init__(self, face_image_list, setting:object):
        super().__init__()
        self.face_image_list = face_image_list
        self.setting = setting

    def run(self):
        model = ai_module.user_detection_net(out_size=2)
        net_scan = ai_module.net_use(model, NET_WEIGHT)
        setting_value = self.setting.page_setting_face_id_complexity_slider
        max_foto_checked_number = 25

        foto_checked_number = math.ceil(max_foto_checked_number*(setting_value+1)/100)
        probability = (50 + math.ceil(50*(setting_value+1)/100))/100
        
        for foto in self.face_image_list[:foto_checked_number]:
            foto_gray = cv.cvtColor(foto, cv.COLOR_RGB2GRAY)
            value, index = net_scan.use(foto_gray)
            if index != 1 or value < probability:
                self.face_id_processing_end.emit(False)

        self.face_id_processing_end.emit(True)

    def stop(self):
        self.quit()
