import cv2
import numpy as np
import matplotlib.pyplot as plt
from image_reader_1 import image_reader
from image_reader_1 import show_image

im = "/home/joemarshal/Downloads/resizedronaldo.jpg"
mode = 0
img = image_reader(im, mode)
plt.hist(img.ravel(), 256, [0, 256])
plt.show()
