import cv2
import numpy as np
from helpers.image_reader import image_reader, show_image

import matplotlib.pyplot as plt

im = "/home/joemarshal/image_processing/images/resizedronaldo.jpg"
mode = 1
img = image_reader(im, mode)
mask = np.zeros(img.shape[:2], np.uint8)
bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)
rect = (50, 50, 400, 267)
show_image(rect)
cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
image = img*mask2[:, :, np.newaxis]
plt.imshow(image), plt.colorbar(), plt.show()
show_image(image)