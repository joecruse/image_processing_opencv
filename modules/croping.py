import numpy as np
import cv2


img = cv2.imread("/home/joemarshal/Downloads/ronaldo.jpg", cv2.IMREAD_COLOR)
cropped = img[70:170, 40:540]
cv2.imshow("croping", cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()