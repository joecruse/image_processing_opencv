import numpy as np
import cv2
from image_reader_1 import image_reader, show_image

img = "/home/joemarshal/Downloads/resizedronaldo.jpg"
mode = cv2.IMREAD_COLOR
im = image_reader(img, 0)
print(im)

print(im.shape)

height, width = im.shape
for h in range(height):
    for w in range(width):
        v = (im[h][w])
        if v < 255:
            im[h][w] = 127
        else:
            im[h][w] = 0
show_image(im)