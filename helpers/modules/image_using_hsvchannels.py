from pprint import pprint

import cv2
import numpy as np
from image_reader_1 import image_reader
from image_reader_1 import show_image


def bgr2hsv(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

def increase_hue_value(cvt2, factor):
    h, w, *no_of_channels = cvt2.shape
    for y in range(h):
        for x in range(w):
            cvt2[y][x][0] = cvt2[y][x][0] + factor
            print(cvt2[y][x][0])
    return cvt2


def increase_saturation_value(cvt1, factor):
    h, w, *no_of_channels = cvt1.shape
    for y in range(h):
        for x in range(w):
            cvt1[y][x][1] = cvt1[y][x][1] + factor
            print(cvt1[y][x][1])
    return cvt1

def increase_value(cvt3, factor):
    h, w, *no_of_channels = cvt3.shape
    for y in range(h):
        for x in range(w):
            cvt3[y][x][2] = cvt3[y][x][2] + factor
            print(cvt3[y][x][2])
    return cvt3


if __name__ == "__main__":
    im = "circles.png"
    mode = 1
    img = image_reader(im, mode)
    cvt = bgr2hsv(img)
    factor = 100

    show_image("ima", cvt)
    # print(cvt[:, :, 0])
    #
    res = increase_hue_value(cvt, factor)
    show_image("increase_h", res)

#
    res1 = increase_saturation_value(cvt, factor)
#     pprint(cvt)
#     print("-------------")
#     pprint(res1)
    show_image("increase_s", res1)

    res2 = increase_value(cvt, factor)
    show_image("increased_v", res2)
#
#
# #show_image("increased_v", res2)
# #res2 = increase_value(cvt, factor)
