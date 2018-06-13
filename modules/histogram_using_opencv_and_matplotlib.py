import cv2
import matplotlib.pyplot as plt
import numpy as np
from helpers.image_reader import image_reader, show_image


if __name__ == "__main__":
    im = "/home/joemarshal/image_processing_opencv/images/resizedronaldo.jpg"
    img = image_reader(im, 0)
    show_image(img)
    mask = np.zeros(img.shape[:2], np.uint8)
    mask[82:328, 31:338] = 255
    masked_img = cv2.bitwise_and(img, img, mask=mask)
    show_image(masked_img)
    hist_full = plt.hist(img.ravel(), 256, [0, 256])
    hist_mask = plt.hist(masked_img.ravel(), 256, [0, 256])
    plt.xlim([0, 256])
    plt.show()
