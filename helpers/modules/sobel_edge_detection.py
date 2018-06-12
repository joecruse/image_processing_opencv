import cv2
import numpy as np
from helpers. image_reader import image_reader, show_image

if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    while(1):
        _, frame = cap.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        sobelx = cv2.Sobel(frame, cv2.CV_64FC1, 1, 0, ksize=5)
        sobely = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize=1)
        laplacian = cv2.Laplacian(frame, cv2.CV_64F, ksize=5)


        cv2.imshow("sobelx", sobelx)
        cv2.imshow("sobely", sobely)
        cv2.imshow("laplacian", laplacian)
        k = cv2.waitKey(100)
        if k == 27:
            break
cv2.destroyAllWindows()
cap.release()
