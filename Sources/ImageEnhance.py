from PIL import ImageEnhance
from PIL import Image
from Config import conf

import numpy as np
import cv2

def enhance_color(im):
    img = ImageEnhance.Contrast(Image.fromarray(im))
    contrasted = img.enhance(conf.contrast)
    converter = ImageEnhance.Color(contrasted)
    colored = converter.enhance(conf.color)
    return np.array(colored)

def crop_image(array, image):
    mask = np.zeros(image.shape, dtype=np.uint8)
    channel_count = image.shape[2]
    ignore_mask_color = (255,) * channel_count
    cv2.fillConvexPoly(mask, array, ignore_mask_color)
    return cv2.bitwise_and(image, mask)
