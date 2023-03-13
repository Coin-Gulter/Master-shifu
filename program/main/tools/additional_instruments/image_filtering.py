import os
import cv2 as cv
import keyboard as kb
import imutils
import multiprocessing

class Process(multiprocessing.Process):
    def __init__(self, file_path, name):
        super(Process, self).__init__()
        self.file_path = file_path
        self.name = name
                 
    def run(self):
        img = cv.imread(self.file_path, cv.IMREAD_COLOR)
        img = imutils.resize(img, width=400)
        cv.imshow(self.name, img)
        cv.waitKey(0)

if __name__ == "__main__":
    print("Впишіть шлях до папки з фото")
    folder_path = input()
    folders = os.listdir(folder_path)

    for folder in folders:
        files = os.listdir(os.path.join(folder_path,folder))
        for file in files:
            file_path = os.path.join(folder_path,folder,file)
            img_name = f'{folder}-{file}'
            proc = Process(file_path, img_name)
            proc.start()
            while True:
                if kb.is_pressed('right'):
                    break
                elif kb.is_pressed('left'):
                    os.remove(file_path)
                    break
            proc.join()