"""
Code to compute the histogram of an image
"""
import cv2
from helpers.image_reader import image_reader, show_image
import matplotlib.pyplot as plt

if __name__ == "__main__":
    img = "/home/joemarshal/image_processing_opencv/images/resizedronaldo.jpg"
    mode = 0
    im = image_reader(img, mode)
    show_image(im)
    cv2.imwrite("/home/joemarshal/grayronaldo.jpg", im)
    hist = cv2.calcHist([im], [0], None, [256], [0, 256])
    print(type(hist))
    show_image(hist)
    plt.show()
