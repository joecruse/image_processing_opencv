import cv2
import numpy as np
from image_reader_1 import image_reader
from image_reader_1 import show_image


img = "/home/joemarshal/Downloads/resizedronaldo.jpg"
mode = cv2.IMREAD_COLOR
im = image_reader(img, mode)
hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
lower_color = np.array([[0, 60, 0]])
upper_color = np.array([255, 150, 255])
mask = cv2.inRange(im, lower_color, upper_color)
#res = cv2.bitwise_and(im, im, mask=mask)
i = show_image(mask)
#i = show_image(res)
#i = show_image(im)
