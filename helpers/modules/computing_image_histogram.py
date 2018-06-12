import cv2
import numpy as np
from image_reader_1 import image_reader
from image_reader_1 import show_image
import matplotlib.pyplot as plt

img = "/home/joemarshal/Downloads/resizedronaldo.jpg"
mode = 0
im = image_reader(img, mode)
show_image(im)

hist = cv2.calcHist([im], [0], None, [256], [0, 256])

print(type(hist))

show_image(hist)
plt.show()