from PIL import ImageEnhance
from PIL import Image
import numpy

def enhance_color(im, contrast, color):
    img = ImageEnhance.Contrast(Image.fromarray(im))
    contrasted = img.enhance(contrast)
    converter = ImageEnhance.Color(contrasted)
    colored = converter.enhance(color)
    return numpy.array(colored)
