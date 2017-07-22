from Config import conf
from Enhance_image import *

import os
import sys
import cv2

class GetData:
    def get_video(self, name):
        self.cap = cv2.VideoCapture(name)
        p = ""
        while not self.cap.isOpened():
            sys.stdout.write("\033[K")
            print("Wait for the header", p, sep='', end="\r", flush=True)
            p = p + "."
            if p == "....":
                p = ""
            cv2.waitKey(1000)
            self.cap = cv2.VideoCapture(name)
        self.total_frames = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))

    def set_position(self, nb):
        pos = self.frame - nb - conf.msec
        if pos < 0:
            pos = 0
        self.cap.set(cv2.CAP_PROP_POS_FRAMES, pos)

    def get_frame(self, nb):
        if self.frame + nb > self.total_frames:
            nb = self.total_frames - self.frame
        self.cap.set(cv2.CAP_PROP_POS_FRAMES, self.frame + nb)
        frame = self.cap.get(cv2.CAP_PROP_POS_FRAMES)
        flag, image = self.cap.read()
        if flag == True:
            dic = {'Frame' : frame, 'Image': enhance_color(image, conf.contrast, conf.color)}
            self.frame += nb
            return dic
        self.cap.set(cv2.CAP_PROP_POS_FRAMES, frame - nb)
        cv2.waitKey(1000)
        print("Error during reading frame: ", self.frame)
        return self.get_frame()

    def __init__(self):
        self.cap = None
        self.frame = 0
        self.total_frames = 0
