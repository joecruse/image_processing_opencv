"""
Here you will see how to change the color image to black and white image using cv2.inRange() function
"""
import cv2
import numpy as np
from helpers.image_reader import image_reader, show_image


if __name__ == "__main__":
    img = "/home/joemarshal/image_processing/images/resizedronaldo.jpg"
    mode = cv2.IMREAD_COLOR

    # Reading the image without any change
    im = image_reader(img, mode)

    # Setting the lower threshold
    lower_color = np.array([[0, 60, 0]])

    # setting the upper threshold
    upper_color = np.array([255, 150, 255])
    mask = cv2.inRange(im, lower_color, upper_color)
    i = show_image(mask)
