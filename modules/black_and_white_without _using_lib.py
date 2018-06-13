"""
Here you can run the threshold of an image without the threshold function
"""

import cv2
from helpers.image_reader import image_reader, show_image



if __name__ == "__main__":
    img = "/home/joemarshal/image_processing_opencv/images/resizedronaldo.jpg"
    mode = cv2.IMREAD_COLOR
    im = image_reader(img, 0)
    print(im)

    print(im.shape)

    height, width = im.shape
    for h in range(height):
        for w in range(width):
            v = (im[h][w])
            if v < 255:
                im[h][w] = 127
            else:
                im[h][w] = 0
    show_image(im)
