import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread("/home/joemarshal/Downloads/ronaldo.jpg", cv2.IMREAD_REDUCED_COLOR_4)
cv2.line(img, (0, 0), (150, 150), (255, 255, 255), 20)
cv2.rectangle(img, (187, 21), (357, 195), (0, 255, 0), 15)
cv2.circle(img, (100, 63), 55, (0, 255, 255), 15)
pyt = np.array([[10, 30], [20, 40], [50, 60], [70, 80]], np.int32)
cv2.polylines(img, [pyt], True, (0, 255, 255), 10)
font = cv2.FONT_ITALIC
cv2.putText(img, "Open CV Tuts!", (10, 20), font, 1, (200, 100, 255), 2,cv2.LINE_AA)
print(img.shape)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
