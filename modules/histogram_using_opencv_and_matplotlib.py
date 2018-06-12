import cv2
import matplotlib.pyplot as plt
import numpy as np
from image_reader_1 import image_reader
from image_reader_1 import show_image

im = "/home/joemarshal/Downloads/resizedronaldo.jpg"
img = image_reader(im, 0)
show_image(img)
mask = np.zeros(img.shape[:2], np.uint8)
mask[82:328, 31:338] = 255
masked_img = cv2.bitwise_and(img, img, mask=mask)
show_image(masked_img)
hist_full = plt.hist(img.ravel(), 256, [0, 256])
hist_mask = plt.hist(masked_img.ravel(), 256, [0, 256])
plt.xlim([0, 256])
plt.show()

