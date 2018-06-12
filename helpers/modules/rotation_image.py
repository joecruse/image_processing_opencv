import cv2
import numpy as np
from image_reader_1 import image_reader
from image_reader_1 import show_image
img = "/home/joemarshal/Downloads/resizedronaldo.jpg"
mode = cv2.WINDOW_NORMAL
im = image_reader(img, mode)
rows, columns = im.shape[:2]
print(rows, columns)
center = (rows/2, columns/2)
rotating_image = cv2.getRotationMatrix2D(center, 570, 1.0)
m = cv2.warpAffine(im, rotating_image, (columns, rows))
i = show_image(m)
