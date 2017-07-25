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
    #roi_corners = np.array([[(10,10), (300,300), (10,300)]], dtype=np.int32)
    # fill the ROI so it doesn't get wiped out when the mask is applied
    channel_count = image.shape[2]  # i.e. 3 or 4 depending on your image
    ignore_mask_color = (255,) * channel_count
    cv2.fillConvexPoly(mask, array, 255, 8, 0)
    # from Masterfool: use cv2.fillConvexPoly if you know it's convex

    # apply the mask
    masked_image = cv2.bitwise_and(image, mask)

    # save the result
    cv2.imshow('prout', ignore_mask_color)#masked_image)
    cv2.waitKey(0)
    #return croped_img
