from __future__ import print_function
import cv2
import numpy as np
from helpers.image_reader import image_reader, show_image
im1 = "/home/joemarshal/Downloads/resizedronaldo.jpg"
mode = 1
img = image_reader(im1, mode)
# show_image(img)

for alpha in np.arange(0, 1.1, 0.1)[::-1]:

        if alpha > 0.0:
            print("transparnet image", alpha)
        else:
            print("Not Transparent", alpha)

        overlay = img.copy()
        output = img.copy()
        cv2.rectangle(overlay, (420, 205), (595, 385), (0, 0, 255), -1)
        cv2.addWeighted(overlay, alpha, output, 1 - alpha, 0, output)
        print("alpha{}, beta{}" .format(alpha, 1 - alpha))

        show_image(output)



