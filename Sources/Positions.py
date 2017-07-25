import numpy as np

def width_compute(width, x):
    return int((width / x) * width / 1280)

def height_compute(height, y):
    return int((height / y) * height / 720)

def get_position_playground(height, width, camera):
    if camera == 0:
        up = [width_compute(width, 1.7), height_compute(height, 1.9)]
        down = [width_compute(width, 2), height_compute(height, 1.1)]
        left = [int(-150 * width / 1280), height_compute(height, 1.3)]
        right = [int(width + 20), height_compute(height, 1.7)]
    else:
        up = [width_compute(width, 9), height_compute(height, 2.8)]
        down = [width_compute(width, 2.4), height_compute(height, 1.8)]
        left = [int(-150 * width / 1280), height_compute(height, 2.3)]
        right = [width_compute(width, 1.4), height_compute(height, 2.3)]
    return np.array([up, left, down, right], dtype=np.int32)
