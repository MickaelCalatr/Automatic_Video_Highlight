import time
import datetime

class Time:
    def need_to_print(self):
        update = self.end - self.need_print
        if update > 0.5:
            self.need_print = self.end
            return True
        return False

    def update(self):
        self.end = time.time()

    def timer(self, frames):
        timer = int(self.end - self.start)
        if self.actu == 0 or timer - self.actu > 3:
            self.total = (timer * self.total_frames) / (frames + 1)
            self.actu = timer
        update = self.end - self.update_f
        if update > 1:
            self.fps = int((frames - self.old_frames) / update)
            self.old_frames = frames
            self.update_f = self.end
        return str("Fps:" + str(self.fps) + "\t\t Time: " + time.strftime("%H:%M:%S", time.gmtime(timer)) + " / " + time.strftime("%H:%M:%S", time.gmtime(self.total)))

    def __init__(self, frames):
        self.fps = 0
        self.old_frames = 0
        self.start = time.time()
        self.end = time.time()
        self.update_f = time.time()
        self.need_print = time.time()
        self.total_frames = int(frames)
        self.total = 0
        self.actu = 0
