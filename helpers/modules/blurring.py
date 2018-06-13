import cv2
import numpy as np

image_loc = "/home/joemarshal/image_processing_opencv/images/resizedronaldo.jpg"


def guassian_blurring(img):
    src = cv2.GaussianBlur(img, (3, 9), cv2.BORDER_DEFAULT)
    cv2.imshow("gaussian bluring", src)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def median_blurring(img):
    src = cv2.medianBlur(img, 3, )
    cv2.imshow("image", src)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def bilateral_blurring(img):
    src = cv2.bilateralFilter(img, 15, 15, 15)
    cv2.imshow("image", src)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    img = cv2.imread(image_loc, cv2.IMREAD_UNCHANGED)

    guassian_blurring(img)
    median_blurring(img)
    bilateral_blurring(img)
