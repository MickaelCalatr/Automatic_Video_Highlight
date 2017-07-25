from PIL import ImageEnhance
from PIL import Image
from Config import conf
from ImageEnhance import *
from Positions import get_position_playground
from log import *
import os
import sys
import cv2
import numpy

_p = "."

def print_points(line):
    global _p
    sys.stdout.write("\033[K")
    print(line, _p, sep='', end="\r", flush=True)
    _p = _p + "."
    if _p == "....":
        _p = "."

class GetData:
    def get_video(self, name):
        self.cap = cv2.VideoCapture(name)
        while not self.cap.isOpened():
            print_points("Wait for the header")
            cv2.waitKey(1000)
            self.cap = cv2.VideoCapture(name)
        self.total_frames = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))

    def set_position(self, nb):
        pos = self.frame - nb - conf.msec
        if pos < 0:
            pos = 0
        self.cap.set(cv2.CAP_PROP_POS_FRAMES, pos)

    def get_frame(self):
        flag = False
        while flag == False:
            nb = conf.fps
            if self.frame + nb > self.total_frames:
                nb = self.total_frames - self.frame
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, self.frame - nb - 1)
            frame = self.cap.get(cv2.CAP_PROP_POS_FRAMES)
            name = str(conf.camera) + "." + str(frame)
            flag, image = self.cap.read()
            if flag == False:
                debug_log(["GET_FRAME", "Frame number:" + str(self.frame), "Total frame:" + str(self.total_frames), "Frame to add:" + str(nb)])
                print_points("Error during reading frame: " + str(self.frame))
                cv2.waitKey(1000)
        if self.frame == 0:
            (h, w, _) = image.shape
            self.playground = get_position_playground(h, w, conf.camera)
        image = crop_image(self.playground, image)
        dic = {'Frame' : frame, 'Name' : name, 'Src': image, 'Image': enhance_color(image)}
        self.frame += nb
        return dic

    def __init__(self):
        self.cap = None
        self.frame = 0
        self.total_frames = 0
        self.playground = None
