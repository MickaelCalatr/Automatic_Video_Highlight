from Config import conf
import heapq
import random
import numpy as np
import cv2

_colors = ["blue", "red", "yellow"]
_detected = [0, 0, 0]

def is_bigger(x, y):
    if _detected[x] > _detected[y]:
        return x, y
    return y, x

def find_colors(data):
    colors = None
    data.get_frame()
    for i in range(20):
        rand = random.randint(0, data.total_frames)#middle - quart, middle + quart)
        data.frame = rand
        frame = data.get_frame()
        detection(frame['Image'])
    big, small = is_bigger(0, 1)
    second, _ = is_bigger(small, 2)
    conf.teams.append(_colors[big])
    conf.teams.append(_colors[second])
    data.set_position(0)
    data.frame = 0

def get_boundaries(index):
    global _colors
    l, u = conf.boundaries[_colors[index]]
    upper = np.array(u)
    lower = np.array(l)
    return lower, upper

def detection(image):
    global _detected
    j = 0
    tmp = image.copy()
    while j < len(conf.boundaries) - 1:
        lower, upper = get_boundaries(j)
        mask = cv2.inRange(tmp, lower, upper)

        (_, cnts, _) = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        try:
            c = max(cnts, key=cv2.contourArea)
            peri = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, 1.05 * peri, True)
            cv2.drawContours(tmp, [approx], -1, (255, 0, 0), 30)
        except ValueError:
            _detected[j] += search(tmp)
            j = j + 1
            tmp = image.copy()

def search(image):
    upper = np.array((255, 0, 0))
    lower = np.array((255, 0, 0))
    mask = cv2.inRange(image, lower, upper)
    (_, cnts, _) = cv2.findContours(mask.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    return len(cnts)
