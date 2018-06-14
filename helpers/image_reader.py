"""
modeule for image reading and showing image
"""

import cv2


def image_reader(img, mode):
    read = cv2.imread(img, mode)
    return read


def show_image(image):
    cv2.imshow("show", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    im = "/home/joemarshal/image_processing_opencv/images/resizedronaldo.jpg"
    mode = 1
    img = image_reader(im, mode)
    show_image(img)
