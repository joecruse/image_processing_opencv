"""
Here is the code to detect the shape in an imaage
"""

import cv2
from helpers.Shapedetector import Shapedetector
from helpers.image_reader import image_reader, show_image
import imutils


if __name__ == "__main__":
    im1 = "/home/joemarshal/image_processing_opencv/images/shapes.jpg"
    mode = 1
    img = image_reader(im1, mode)
    show_image(img)
    cv2.imwrite("/home/joemarshal/shapes.png", img)
    resized = imutils.resize(img, width=300)
    ratio = img.shape[0] / float(resized.shape[0])
    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]
    edges = cv2.Canny(thresh, 75, 150)
    show_image(edges)
    show_image(thresh)
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if imutils.is_cv2() else cnts[1]
    sd = Shapedetector()
    for c in cnts:
        M = cv2.moments(c)
        cx = int((M["m10"] / M["m00"]) * ratio)
        cy = int((M["m01"] / M["m00"]) * ratio)
        shape = sd.detect(c)
        c = c.astype("float")
        c *= ratio
        c = c.astype("int")
        cv2.drawContours(img, [c], -1, (0, 255, 0), 2)
        cv2.putText(img, shape, (cx, cy), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
        show_image(img)
