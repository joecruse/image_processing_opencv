"""
Here you will see how to add two images without the cv2.add() function
"""
from helpers.image_reader import image_reader, show_image


def adding_images_without_add_function(imag1, imag2):
    """
    :param imag1: passing image1
    :param imag2: passing image 2
    :return: adds both the images
    """
    add1 = imag1+imag2
    return add1


if __name__ == "__main__":
    im1 = "/home/joemarshal/image_processing/images/resizedronaldo.jpg"
    im2 = "/home/joemarshal/image_processing/images/resizedmessi.jpg"
    mode = 1
    img1 = image_reader(im1, mode)
    img2 = image_reader(im2, mode)
    add = adding_images_without_add_function(img1, img2)
    show_image(add)
