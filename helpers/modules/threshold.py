import cv2
import numpy as np

from cv2_helpers import show_image, read_image

if __name__ == "__main__":
    img = read_image("/home/joemarshal/Downloads/resizedronaldo.jpg", cv2.IMREAD_COLOR)
    rows, columns, channels = img.shape
    roi = img[0:rows, 0:columns]
    img2gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV)
    show_image(img2gray)
