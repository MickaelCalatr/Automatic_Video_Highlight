from PIL import ImageEnhance
from PIL import Image
from Config import conf
import os
import sys
import cv2
import numpy

class GetData:
    def get_video(self, name):
        print(name)
        self.cap = cv2.VideoCapture(name)
        print(name)
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
        pos = self.frame - nb - self.msec
        if pos < 0:
            pos = 0
        self.cap.set(cv2.CAP_PROP_POS_FRAMES, pos)

    def get_frame(self):
        nb = 15
        if self.frame + 15 > self.total_frames:
            nb = self.total_frames - self.frame
        self.cap.set(cv2.CAP_PROP_POS_FRAMES, self.frame + nb)
        frame = self.cap.get(cv2.CAP_PROP_POS_FRAMES)
        name = str(self.camera) + "." + str(frame)
        flag, image = self.cap.read()
        if flag == True:
            dic = {'Frame' : frame, 'Name' : name, 'Src': image, 'Image': self.enhance_color(image)}
            self.frame += nb
            return dic
        self.cap.set(cv2.CAP_PROP_POS_FRAMES, frame - nb)
        cv2.waitKey(1000)
        print("Error during reading frame: ", self.frame)
        return self.get_frame()

    def get_big_frame(self, nb):
        if self.frame + 15 > self.total_frames:
            nb = self.total_frames - self.frame
        self.cap.set(cv2.CAP_PROP_POS_FRAMES, self.frame + nb - 1)
        frame = self.cap.get(cv2.CAP_PROP_POS_FRAMES)
        name = str(self.camera) + "." + str(frame)
        flag, image = self.cap.read()
        if flag == True:
            dic = {'Frame' : frame, 'Name' : name, 'Src': image, 'Image': self.enhance_color(image)}
            self.frame += nb
            return dic
        self.cap.set(cv2.CAP_PROP_POS_FRAMES, frame - nb - 1)
        cv2.waitKey(1000)
        return self.get_big_frame(nb)

    def enhance_color(self, im):
        img = ImageEnhance.Contrast(Image.fromarray(im))
        contrast = img.enhance(self.contrast)
        converter = ImageEnhance.Color(contrast)
        colored = converter.enhance(self.color)
        return numpy.array(colored)

    def __init__(self):
        self.img_written = 0
        self.cap = None
        self.frame = 0
        self.msec = conf.msec
        self.camera = int(conf.camera)
        self.total_frames = 0
        self.position = 0

        # ENHANCE_COLOR
        self.contrast = 1.3
        self.color = 1
