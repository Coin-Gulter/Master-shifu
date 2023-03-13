import random
import time
import cv2 as cv
import os
import json
import numpy as np
import unicodedata
import string

# program modules
# from . import face_detection_module
# from ..operative_info_instruments import array_additional_module

import face_detection_module
import array_additional_module_test

CURRENT_WORKING_DIRECTORY = os.getcwd()
FACE_DT_PATH = CURRENT_WORKING_DIRECTORY + r'\program\data\face_id_data\filtered_face_dt'
FACE_JSON_TARGET_PATH = CURRENT_WORKING_DIRECTORY + r'\program\data\face_id_data\target_json\face_id_target_2.json'
FACE_JSON_TARGET_PASS_PATH = CURRENT_WORKING_DIRECTORY + r'\program\data\face_id_data\target_json\face_pass_target_2.json'
ALL_CHARACTERS = string.ascii_letters + " .,;'()/_=-!?:"
EOS = 128

def unicodeToAscii(string):
    return ''.join(c for c in unicodedata.normalize('NFD', string) if unicodedata.category(c) != 'Mn' and c in ALL_CHARACTERS)

def string_to_number_list(string):
    return [ ord(char) for char in list(string)]

def generate_random_pass():
    pass_len = 20
    pass_string = ""
    for _ in range(pass_len):
        pass_string = pass_string + random.choice(ALL_CHARACTERS)
    return pass_string


def preper_face_id_target_dt_set(password, path=FACE_DT_PATH, face_target_path=FACE_JSON_TARGET_PATH, face_target_pass_path=FACE_JSON_TARGET_PASS_PATH):
    print('prepered working directory_________________', os.getcwd())
    folders_name = os.listdir(path)
    faces_id_dt = {}
    faces_pass_dt = {}

    for folder in folders_name:
        folder_path = os.path.join(path, folder)
        id_list = [0]

        if folder == 'client':
            id = 1
            password = string_to_number_list(unicodeToAscii(password))
            password.append(EOS)
            faces_pass_dt[id] = password
        else:
            id = 0
            pass_string = '0000000000'
            other_pass = [ord(char) for char in pass_string]
            other_pass.append(EOS)
            faces_pass_dt[id] = other_pass

        id_list[0] = id
        faces_id_dt[(f"{folder_path}\\")] = id_list

    json_file = json.dumps(faces_id_dt)
    with open(face_target_path, 'w') as f:
        f.write(json_file)

    json_pass_file = json.dumps(faces_pass_dt)
    with open(face_target_pass_path, 'w') as f:
        f.write(json_pass_file)


def load_random_prepered_obj_from_recognize_dt_set(number=100, target_path=FACE_JSON_TARGET_PATH):
 
    pairs = []

    with open(target_path, 'r') as openfile:
        target_dict = json.load(openfile)

    for _ in range(number):
        pair = []
        random_target_folder, _ = random.choice(list(target_dict.items()))
        random_target_id = array_additional_module_test.getFromDict(target_dict, random_target_folder)
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

def load_random_prepered_obj_from_password_dt_set(number=100, target_path=FACE_JSON_TARGET_PASS_PATH):
 
    pairs = []

    with open(target_path, 'r') as openfilepass:
        target_dict = json.load(openfilepass)

    for _ in range(number):
        pair = []
        random_target_id, _ = random.choice(list(target_dict.items()))
        target_pass = array_additional_module_test.getFromDict(target_dict, random_target_id)
        print('random_target_id_______________', target_pass)
        print('random_target_folder_______________', random_target_id)
        
        pair.append(random_target_id)
        pair.append(target_pass)
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
    preper_face_id_target_dt_set('Harley')
    print(load_random_prepered_obj_from_password_dt_set(10, target_path=FACE_JSON_TARGET_PATH, target_pass_path=FACE_JSON_TARGET_PASS_PATH))
