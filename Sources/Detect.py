from Rate import RateImage
from Time import Time
from Config import conf
from SaveData import *

import Folder
import shutil
import threading
import sys
import numpy as np
from shutil import copyfile
import cv2

class Detect:
    def get_boundaries(self, index):
        l, u = conf.boundaries[conf.teams[index]]
        upper = np.array(u)
        lower = np.array(l)
        return lower, upper

    def initialize(self):
        Folder.create("./tmp/")
        self.time = Time(self.data.total_frames)

    def take_section(self):
        self.data.set_position(conf.max_thread)
        self.time.old_frame = self.data.frame
        i = 0
        keep = True
        max_player = 0
        start_frame = self.data.frame
        while (self.data.frame < self.data.total_frames and keep == True) or (self.data.frame < self.data.total_frames and i < conf.msec):
            frame = self.data.get_frame()
            keep, rate = self.loop(frame)
            if keep:
                i = 0
            else:
                if self.data.frame + conf.fps < self.data.total_frames:
                    i += conf.fps
                else:
                    i += self.data.total_frames - self.data.frame
            if max_player < len(rate.players):
                max_player = len(rate.players)
            self.time.update()
        t = threading.Thread(target=save_doc, args=(start_frame, self.data.frame, max_player,))
        self.threads.append(t)
        self.file_saved += 1
        t.start()

    def run(self):
        self.initialize()
        while self.data.frame < self.data.total_frames:
            frame = self.data.get_frame()
            keep, _ = self.loop(frame)

            if keep == True:
                self.take_section()
            self.time.update()
        print()
        for x in self.threads:
            x.join()

    def loop(self, frame):
        if self.time.need_to_print():
            sys.stdout.write("\033[F\033[J\033[F\033[J\033[F\033[J")
            print("Files saved:\t", self.file_saved)
            print("Frame:\t\t", self.data.frame, "/", self.data.total_frames)
            print(self.time.timer(int(frame['Frame'])))

        keep, rate = self.detection(frame)
        return keep, rate

    def detection(self, frame):
        image = frame['Image']
        final_img = None
        if conf.debug:
            final_img = image.copy()
        j = 0
        while j < len(conf.teams):
            lower, upper = self.get_boundaries(j)
            mask = cv2.inRange(image, lower, upper)

            (_, cnts, _) = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            try:
                c = max(cnts, key=cv2.contourArea)
                peri = cv2.arcLength(c, True)
                approx = cv2.approxPolyDP(c, 1.05 * peri, True)

                cv2.drawContours(image, [approx], -1, conf.point_color[j], 30)
            except ValueError:
                j = j + 1
        if conf.debug:
            keep, rate, img_debug = self.search(image, final_img, frame['Frame'])
            cv2.imshow('Features', img_debug)
            cv2.waitKey(0)
            return keep, rate
        else:
            keep, rate, _ = self.search(image, final_img, frame['Frame'])
            return keep, rate


    def search(self, image, final_image, index):
        rate = RateImage(image.shape, conf.camera)
        image_tmp = None
        if conf.debug:
            image_tmp = final_image.copy()

        for j in range(0, len(conf.teams)):
            upper = np.array(conf.point_color[j])
            lower = np.array(conf.point_color[j])
            mask = cv2.inRange(image, lower, upper)
            (_, cnts, _) = cv2.findContours(mask.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            for k in range(0, len(cnts)):
                cnt = cnts[k]
                x, y, w, h = cv2.boundingRect(cnt)
                rate.add_player(x, y, h, w)
                if conf.debug:
                    cv2.rectangle(image_tmp, (x, y), (x + w, y + h), (0, 0, 255), 2)
                    cv2.polylines(image_tmp, [rate.points], True, (0, 0, 255), 2)
        return rate.rate_img(), rate, image_tmp


    def __init__(self, data):
        self.data = data
        self.time = None
        self.file_saved = 0
        self.threads = []
