"""
Here you will see the class code for shape detectors
"""
import cv2
import numpy as np


class Shapedetector:
    def __init__(self):
        pass

    def detect(self, c):
        """

        :param c: outline of the shape we are trying to find
        :return:
        """
        shape = "unidentified"
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.04 * peri, True)

        if len(approx) == 3:
            shape = "triangle"

        elif len(approx) == 4:
            (x, y, w, h) = cv2.boundingRect(approx)
            shape = "rectangle"

            ar = w / float(h)

            shape = "square" if ar >= 0.95 and ar <= 1.05 else "rectangle"


        elif len(approx) == 5:
            shape = "pentagon"

git 
        elif len(approx):
            shape = "circle"

        return shape
