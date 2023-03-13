import numpy as np


separateArrElem = lambda array, separator: [ string.split(separator) for string in array ]

def make_list_from_elem(elem):
    arr = []
    arr.append(elem)
    return arr

def getFromDict(diction, value):
    for key in diction:
        if key==value:
            return diction[key]
        elif diction[key]==value:
            return key

def connect_dict(dict1, dict2):
    new_array = []
    for key in dict1:
        temp = []
        temp.append(dict1[key])
        temp.append(dict2[key])
        new_array.append(temp)
    return new_array

def dict_str_to_int(dict_inp, dict_rule):
    new_dict = {}
    for key in dict_inp:
        new_dict[key] = make_list_from_elem(getFromDict(dict_rule, dict_inp[key]))
    return new_dict

def compare_arr(arr1, arr2):
    right, wrong = np.empty(shape=(1),dtype=np.float32), np.empty(shape=(1),dtype=np.float32)
    for (elem1, elem2) in zip(arr1, arr2):
        # print("compare elem_____", elem1, elem2)
        if elem1 == elem2:
            right = np.append(right, elem1)
            # print("right added___", right)
        else:
            wrong = np.append(wrong, elem1)
            # print("wrong added___", right)
    return right, wrong




if __name__ == "__main__":
    pass
