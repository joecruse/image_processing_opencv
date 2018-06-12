import cv2
import numpy as np

img1 = cv2.imread("/home/joemarshal/Downloads/ronaldo.jpg", cv2.IMREAD_COLOR)
img2 = cv2.imread("/home/joemarshal/Downloads/messi.jpg", cv2.IMREAD_COLOR)


print("dimension of the 1 given picture :", img1.shape)
print("dimension of the 2 given picture :", img2.shape)


width = 500
height = 500

res = (width, height)

resize1 = cv2.resize(img1, res, interpolation=cv2.INTER_AREA)
resize2 = cv2.resize(img2, res, interpolation=cv2.INTER_AREA)

print("resized1 dimensions:", resize1.shape)
print("resized2 dimensions:", resize2.shape)


cv2.imshow("resizedronaldo", resize1)
cv2.imshow("resizedmessi", resize2)
cv2.imwrite("/home/joemarshal/Downloads/resizedronaldo.jpg", resize1)
cv2.imwrite("/home/joemarshal/Downloads/resizedmessi.jpg", resize2)
cv2.waitKey(0)
cv2.destroyAllWindows()