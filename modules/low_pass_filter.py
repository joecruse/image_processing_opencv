"""
Here you will find the code for low-pas-filter
"""
import cv2
from helpers.image_reader import image_reader, show_image


def low_pass_filter(img):
    """

    :param img:
    :return:
    """
    fil = cv2.boxFilter(img, -1, (57, 57))
    return fil


if __name__ == "__main__":
    path = "/home/joemarshal/image_processing_opencv/images/shapes.jpg"
    mode = 1
    ima = image_reader(path, mode)
    show_image(ima)
    con = cv2.cvtColor(ima, cv2.COLOR_BGR2RGB)
    show = low_pass_filter(con)
    show_image(show)
