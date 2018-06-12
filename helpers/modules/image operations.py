import numpy as np
import cv2
import matplotlib.pyplot as plt
img = cv2.imread("/home/joemarshal/Downloads/ronaldo.jpg", cv2.IMREAD_REDUCED_COLOR_4)


img[55, 55] =[255, 255, 255]
px = img[55, 55]

print(px)
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


