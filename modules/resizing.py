import numpy as np
import cv2


def resizing(width=None, height=None):
    pass


if __name__ == "__main__":
    img = cv2.imread("/home/joemarshal/Downloads/messi.jpg", cv2.IMREAD_REDUCED_COLOR_4)
    width = int(input())
    height = int(input())
    r = width / img.shape[1]
    dim = (height, int(img.shape[0] * r))
    resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    cv2.imshow("resize", resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
