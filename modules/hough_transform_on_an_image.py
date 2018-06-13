"""
Here you will see the code for hough_transformation in an image
"""
import cv2
import numpy as np
from helpers.image_reader import image_reader, show_image


def hough_transform_image(image, img):
    """

    :param image: pass the canny iamge
    :param img: pass the original image
    :return: it will mark the lines in the canny image and passes it back to the original image
    """
    lines = cv2.HoughLinesP(image, 1, np.pi/180, 50, maxLineGap=200)
    for line in lines:
        print(line)
        x1, x2, y1, y2 = line[0]
        cv2.line(img, (x1, x2), (y1, y2), (0, 255, 0), 3)

    show_image(img)
    return lines


if __name__ == "__main__":
    img1 = "/home/joemarshal/image_processing_opencv/images/lines.png"
    mode = 0
    image1 = image_reader(img1, 1)
    grey = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(grey, 75, 150)
    show_image(edges)
    hough = hough_transform_image(edges, image1)


