"""
Here you can find how to add to images using the cv2.add() function
"""

import cv2
from helpers.image_reader import image_reader, show_image


def add_image(image1, image2):
    """
    :param image1: passing image1
    :param image2: passing image 2

    :return: adds both the images
    """
    add = cv2.add(image1, image2)
    return add


if __name__ == "__main__":
    img1 = "/home/joemarshal/image_processing/images/resizedronaldo.jpg"
    img2 = "/home/joemarshal/image_processing/images/resizedmessi.jpg"
    mode = 1
    img1 = image_reader(img1, mode)
    img2 = image_reader(img2, mode)
    adding = add_image(img1, img2)
    show_image(adding)


