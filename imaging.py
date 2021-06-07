import mss
from PIL import Image
import pytesseract

import constants

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
sct = mss.mss()


def get_image(box):
    img = sct.grab(constants.BOXES['portraits'])
    return Image.frombytes("RGB", img.size, img.bgra, 'raw', 'BGRX')


def screenshot_portraits():
    return get_image(constants.BOXES['portraits'])


def convert_to_text(img):
    return pytesseract.image_to_string(img)
