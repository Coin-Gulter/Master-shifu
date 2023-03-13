import os
import re
import pandas as pd
import psutil
import hashlib
import base64
import cryptography
from cryptography.fernet import Fernet as fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

FILE_PATH = '.\\'


class Hash_files():

    def __init__(self, file_path=FILE_PATH, hashed_files_name="file_info.csv",  hash_file_format='dfd',  salt_length=16):
        self.file_path = file_path
        self.encrypted_file_format = hash_file_format
        self.salt_length = salt_length

        # Regular expression to find a file format in string
        self.file_format_re = re.compile(r'(?<=\.)[^\\.]([^.]+)$')
        # Regulsr expression to find a file name with format in string
        self.file_name_re = re.compile(r'(?<=\/)?[^\/]+(\.[^\/]+)$')

        self.basic_key = b'tjipwRDuoyp49d5_7-2qkPu0uxeU-FuYKXec6HF_lJM='
        self.basic_salt = b'\xd2\xb7\xb7\xf8\x05`\x96J\x99\x85HaH<\xd6\xe6'


    def get_user_salt(self, user_name):
        with open(os.path.join(self.file_path, user_name+'-S.byt'), 'rb') as file_salt:
            return file_salt.read()

    def get_user_pass(self, user_name):
        with open(os.path.join(self.file_path, user_name+'-P.byt'), 'rb') as file_pass:
            return file_pass.read()

    def string_hashing(self, string):
        return hashlib.sha512(string).digest()

    # function that make encrypted key
    def password_2_hashkey(self, password, salt=None):
        if salt == None:
            salt = self.basic_salt
        kdf = PBKDF2HMAC(algorithm=hashes.SHA512(), length=32, salt=salt, iterations=480000)
        pass_hash = kdf.derive(password)
        key = base64.urlsafe_b64encode(pass_hash).decode()
        return key
    
    def add_new_pass_salt_to_hash(self, user_name, password):
        # generate salt, file names and test password hash
        salt = os.urandom(self.salt_length)
        pass_hash = self.string_hashing(password)
        file_pass_name = user_name + '-P.byt'
        file_salt_name = user_name + '-S.byt'

        # write salt and password hash to two different files
        with open(os.path.join(self.file_path, file_pass_name), 'wb') as file_pass:
            file_pass.write(pass_hash)
        with open(os.path.join(self.file_path, file_salt_name), 'wb') as file_salt:
            file_salt.write(salt)

    def encrypto_file(self, hash_key, start_file_path=None, end_path=None, delete_source_file=False):

        # Check enough free memory to encrypt or not
        if os.path.getsize(start_file_path) >= psutil.virtual_memory()[4]:
            raise Exception("file size too much to encrypt. Not enough free virtual memory")
        else:
            fr = fernet(hash_key)

            # opening the original file to encrypt
            with open(start_file_path, 'rb') as file:
                original_file = file.read()
                
            # encrypting the file
            encrypted_file = fr.encrypt(original_file)

            # make end file path
            end_file_path = os.path.join(end_path, ('(' + os.path.basename(start_file_path) + ').' + self.encrypted_file_format))

            # write encrypted file in the path
            with open(end_file_path, 'wb') as encrypt_file:
                encrypt_file.write(encrypted_file)

            # delete existed file
            if delete_source_file:
                os.remove(start_file_path)

            return 1 

    
    def decrypto_file(self, hash_key, start_file_path=None, end_path=None, delete_source_file=False):

        # Check enough free memory to encrypt or not
        if os.path.getsize(start_file_path) >= psutil.virtual_memory()[4]:
            raise Exception("file size too much to decrypt. Not enough free virtual memory")
        else:
            fr = fernet(hash_key)

            # opening the original file to decrypt
            with open(start_file_path, 'rb') as file:
                original_file = file.read()
                
            # decrypting the file
            try:
                decrypted_file = fr.decrypt(original_file)
            except cryptography.fernet.InvalidToken:
                return False

            # make end file path
            file_name = os.path.basename(start_file_path)
            end_file_name = re.sub( r'\(', '', file_name)
            end_file_name = re.sub(r'\).dfd$', '', end_file_name)
            end_file_path = os.path.join(end_path, end_file_name)

            # opening the file in write mode and
            # writing the encrypted data
            with open(end_file_path, 'wb') as decrypt_file:
                decrypt_file.write(decrypted_file)

            # delete existed file
            if delete_source_file:
                os.remove(start_file_path)

            return True







if __name__ == "__main__":
    password = "6"
    user = 'testname'
    password = bytes(password, 'utf-8')

    crypto_file = Hash_files()
    crypto_file.password_2_hashkey(password)
    # # pass_hash = crypto_file.get_user_pass(user)
    # salt = crypto_file.get_user_salt(user)
    # your_hash = crypto_file.string_hashing(password)

    # if your_hash == pass_hash:
    #     key = crypto_file.password_2_hashkey(password, salt)
    #     crypto_file.encrypto_file(key, r'D:\Projects\PC_defender\code\test3.jpg')
    #     crypto_file.decrypto_file(key, r'D:\Projects\PC_defender\code\test3.dfd')
