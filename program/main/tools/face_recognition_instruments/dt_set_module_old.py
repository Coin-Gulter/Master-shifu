import random
import time
import cv2 as cv
import os
import json
import numpy as np

# program modules
from . import face_detection_module
from ..operative_info_instruments import array_additional_module_old


FACE_DT_PATH = r'..\..\..\data\face_id_data\filtered_face_dt'
FACE_JSON_TARGET_PATH = r'..\..\..\data\face_id_data\target_json\face_id_target.json'

def preper_face_id_target_dt_set(path=FACE_DT_PATH, face_target_path=FACE_JSON_TARGET_PATH):
    print('prepered working directory_________________', os.getcwd())
    folders_name = os.listdir(path)
    faces_id_dt = {}

    for folder in folders_name:
        folder_path = os.path.join(path, folder)
        id_list = [0]*2
        if folder == 'other':
            id = 0
        else:
            id = 1
        id_list[id] = 100
        faces_id_dt[(f"{folder_path}\\")] = id_list

    json_file = json.dumps(faces_id_dt)
    with open(face_target_path, 'w') as f:
        f.write(json_file)


def load_random_prepered_obj_from_dt_set(number=100, target_path=FACE_JSON_TARGET_PATH):
 
    pairs = []

    with open(target_path, 'r') as openfile:
        target_dict = json.load(openfile)

    for _ in range(number):
        pair = []
        random_target_folder, _ = random.choice(list(target_dict.items()))
        random_target_id = array_additional_module_old.getFromDict(target_dict, random_target_folder)
        print('random_target_id_______________', random_target_id)
        print('random_target_folder_______________', random_target_folder)

        random_target_file = random.choice(os.listdir(random_target_folder))
        file_path = os.path.join(random_target_folder, random_target_file)

        img = cv.imread(file_path, cv.IMREAD_COLOR)
        img_rgb = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

        pair.append(img_rgb)
        pair.append(random_target_id)
        pairs.append(pair)
    return pairs


def save_client_face( faces:list ,folder_path=FACE_DT_PATH, client_folder_name=r'client'):
    folder_client_path = os.path.join(folder_path, client_folder_name)
    file_number = 0

    for face in faces:
        file = f'({file_number}).jpg'
        file_path = os.path.join(folder_client_path, file)

        if os.path.exists(folder_path):

            if os.path.exists(file_path):

                if random.randint(0,1):     
                    cv.imwrite(file_path, face)
            else:
                cv.imwrite(file_path, face)
        else:
            return 0, 'folder path not found'
        file_number += 1
    return 1


if __name__ == "__main__":
    pass
