"""
Here you will see the basic arithmetic operations done such bitwise and etc

"""
import cv2
from helpers.image_reader import image_reader, show_image


def bitwise_and(img1, img2):
    """

    :param img1: pass image 1
    :param img2: pass image 2
    :return: returns the bitwise and of both the images
    """

    return cv2.bitwise_and(img1, img2)


def bitwise_or(img1, img2):
    """

    :param img1: pass image 1
    :param img2: pass image 2
    :return: returns the bitwise or of both the images
    """

    return cv2.bitwise_or(img1, img2)


def bitwise_not(img1, img2):
    """

    :param img1: pass image 1
    :param img2: pass image 2
    :return: returns the bitwise not of both the images
    """

    return cv2.bitwise_not(img1, img2)


def bitwise_xor(img1, img2):
    """

    :param img1: pass image 1
    :param img2: pass image 2
    :return: returns the bitwise xor of both the images
    """

    return cv2.bitwise_xor(img1, img2)


def subtract(img1, img2):
    """

    :param img1: pass image 1
    :param img2: pass image 2
    :return: returns the subtract of both the images
    """

    return cv2.subtract(img1, img2)


def multiplication(img1, img2):
    """

    :param img1: pass image 1
    :param img2: pass image 2
    :return: returns the multiplication of both the images
    """
    return cv2.multiply(img1, img2)


def division(img1, img2):
    """

    :param img1: pass image 1
    :param img2: pass image 2
    :return: returns the division of both the images
    """
    return cv2.divide(img1, img2)


if __name__ == "__main__":
    im1 = "/home/joemarshal/image_processing/images/resizedronaldo.jpg"
    im2 = "/home/joemarshal/image_processing/images/resizedmessi.jpg"
    mode = cv2.WINDOW_NORMAL
    image1 = image_reader(im1, mode)
    image2 = image_reader(im2, mode)
    show_image(image1)
    show_image(image2)
    bit_and = bitwise_and(image1, image2)
    bit_or = bitwise_or(image1, image2)
    bit_not = bitwise_not(image1, image2)
    bit_xor = bitwise_xor(image1, image2)
    subt = subtract(image1, image2)
    mul = multiplication(image1, image2)
    div = division(image1, image2)
    show_image(bit_and)
    show_image(bit_or)
    show_image(bit_not)
    show_image(bit_xor)
    show_image(subt)
    show_image(mul)
    show_image(div)
