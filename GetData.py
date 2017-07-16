from PIL import ImageEnhance
from PIL import Image
from Config import conf
import os
import sys
import cv2
import numpy

class GetData:
    def get_video(self, name):
        self.cap = cv2.VideoCapture(name)
        p = ""
        while not self.cap.isOpened():
            self.cap = cv2.VideoCapture(name)
            cv2.waitKey(1000)
            sys.stdout.write("\033[K")
            print("Wait for the header", p, sep='', end="\r", flush=True)
            p = p + "."
            if p == "....":
                p = ""
        self.total_frames = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))

    def set_position(self, nb):
        pos = self.frame - nb - self.msec
        if pos < 0:
            pos = 0
        self.cap.set(cv2.CAP_PROP_POS_FRAMES, pos)

    def get_frame(self):
        self.cap.set(cv2.CAP_PROP_POS_FRAMES, self.frame + 15)
        frame = self.cap.get(cv2.CAP_PROP_POS_FRAMES)
        name = str(self.camera) + "." + str(frame)
        flag, image = self.cap.read()
        if flag == True:
            dic = {'Frame' : frame, 'Name' : name, 'Src': image, 'Image': self.enhance_color(image)}
            #self.elems.append(dic)
            #self.size += 1
            self.frame += 15
            return dic
        self.cap.set(cv2.CAP_PROP_POS_FRAMES, frame - 15)
        cv2.waitKey(1000)
        print("Error during reading frame: ", self.frame)
        return self.get_frame()

    def get_big_frame(self, nb):
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

    def write_frames(self, start, end):
        #print("Save")
        name = conf.video_source[conf.camera]
        end = (end - start) / 25
        start_point = start / 25
        #print("ffmpeg -r 25 -i " + name +" -ss " + str(start_point) + " -c copy -t " + str(end) + " ./tmp/" + str(start) + ".mp4")
        os.system("ffmpeg -loglevel quiet -r 25 -i " + name +" -ss " + str(start_point) + " -c copy -t " + str(end) + " ./tmp/" + str(start) + ".mp4")
        self.size = 0
        self.elems.clear()
        #if len(self.elems) > 0:
        #   while len(self.elems) > 0:
        #        cv2.imwrite("./tmp/pic" + '{0:07}'.format(self.img_written) + ".png", self.elems.pop(0)['Src'])
        #        self.img_written += 1
        #    self.size = 0

    def __init__(self):
        self.img_written = 0
        self.cap = None
        self.elems = []
        self.size = 0
        self.frame = 0
        self.msec = conf.msec
        self.camera = int(conf.camera)
        self.total_frames = 0
        self.position = 0

        # ENHANCE_COLOR
        self.contrast = 1.3
        self.color = 1
