import numpy as np
import cv2

img = cv2.imread("/home/joemarshal/Downloads/resizedronaldo.jpg", cv2.IMREAD_UNCHANGED)

src = cv2.GaussianBlur(img, (3, 9), cv2.BORDER_DEFAULT)

cv2.imshow("gaussian bluring", src)
cv2.waitKey(0)
cv2.destroyAllWindows()
