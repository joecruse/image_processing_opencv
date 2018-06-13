import cv2
from helpers.image_reader import image_reader, show_image


if __name__ == "__main__":
    img = "/home/joemarshal/image_processing_opencv/images/resizedronaldo.jpg"
    mode = cv2.WINDOW_NORMAL
    im = image_reader(img, mode)
    rows, columns = im.shape[:2]
    print(rows, columns)
    center = (rows/2, columns/2)
    rotating_image = cv2.getRotationMatrix2D(center, 570, 1.0)
    m = cv2.warpAffine(im, rotating_image, (columns, rows))
    i = show_image(m)
