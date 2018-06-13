"""
Here you will see the code for thresholding an image
"""
import cv2
from helpers.image_reader import show_image


if __name__ == "__main__":
    img = cv2.imread('/home/joemarshal/image_processing_opencv/images/resizedronaldo.jpg', 0)
    ret, thresh_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    i = show_image(thresh_img)
    cv2.imwrite("/home/joemarshal/image_processing_opencv/images/thresholdronaldo.jpg", thresh_img)
