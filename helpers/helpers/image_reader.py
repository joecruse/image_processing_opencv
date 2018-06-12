import cv2


def image_reader(img, mode):
    """

    :param img: pass the image path
    :param mode: pass the mode of the image to be displayed
    :return: passes back the read function
    """
    return cv2.imread(img, mode)


def show_image(img):
    """

    :param img: pass the image
    :return: displayes the image
    """
    cv2.namedWindow("Show", cv2.WINDOW_NORMAL)
    cv2.imshow("Show", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    img1 = ""
    mode1 = 0
    im = image_reader(img1, mode1)
    show_image(im)
