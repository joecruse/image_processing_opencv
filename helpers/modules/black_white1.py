import cv2
import numpy as np
from image_reader_1 import show_image
img = cv2.imread('/home/joemarshal/Downloads/resizedronaldo.jpg', 0)
ret, thresh_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
i = show_image(thresh_img)