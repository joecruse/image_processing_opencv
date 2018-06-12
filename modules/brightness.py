import cv2
import numpy as np
from image_reader_1 import show_image

img = cv2.imread("/home/joemarshal/Downloads/resizedronaldo.jpg", 1)

alpha = 2
beta = 10

result = cv2.addWeighted(img, alpha, np.zeros(img.shape, img.dtype), 0, beta)
show_image(result)
cv2.imwrite("/home/joemarshal/Documents/bc.jpg", result)
cv2.waitKey(0)
cv2.destroyAllWindows()

