import os
import string
import unicodedata

path = 'C:/Users/Volodia/Downloads/untitled.ui.dfd'
all_letters = string.ascii_letters + " .,;'()/_=-!?:"

def unicodeToAscii(s):
    return ''.join(
        c for c in unicodedata.normalize('NFD', s)
        if unicodedata.category(c) != 'Mn'
        and c in all_letters
    )

def print_all_acsii_chars():
    for num in range(128):
        print(chr(num))

if __name__ == '__main__':
    # print(ord(unicodeToAscii('a')[0]))
    # print(chr(0))
    # print(len(all_letters))
    # print_all_acsii_chars()
    print(

