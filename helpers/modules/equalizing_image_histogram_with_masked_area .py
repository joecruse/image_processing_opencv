import numpy as np
import cv2
from image_reader_1 import image_reader
from image_reader_1 import show_image

im = "/home/joemarshal/Downloads/resizedronaldo.jpg"
mode = 0
img = image_reader(im, mode)
show_image(img)
mask = np.zeros(img.shape[:2], np.uint8)
mask[82:328, 31:338] = 255
masked_img = cv2.bitwise_and(img, img, mask=mask)
equal = cv2.equalizeHist(img)
mask1 = cv2.equalizeHist(masked_img)
res = np.hstack((img, equal, mask1))
show_image(res)
cv2.imwrite("/home/joemarshal/Downloads/equal_hist.png", res)