"""
Here you can find the code for the brightness of the image
"""


import cv2
import numpy as np
from helpers.image_reader import show_image


if __name__ == "__main__":
    img = cv2.imread("/home/joemarshal/image_processing_opencv/images/resizedronaldo.jpg", 1)
    alpha = 2
    beta = 10
    result = cv2.addWeighted(img, alpha, np.zeros(img.shape, img.dtype), 0, beta)
    show_image(result)
    cv2.imwrite("/home/joemarshal/Documents/bc.jpg", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
