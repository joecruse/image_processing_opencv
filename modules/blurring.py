import cv2

image_loc = "/home/joemarshal/image_processing_opencv/images/resizedronaldo.jpg"


def guassian_blurring(img):

    """

    :param img:pass the image
    :return:Gaussian blurring
    """
    src = cv2.GaussianBlur(img, (3, 9), cv2.BORDER_DEFAULT)
    cv2.imshow("gaussian bluring", src)
    cv2.imwrite("/home/joemarshal/image_processing_opencv/images/Gaussian_blurring.jpg", src)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def median_blurring(img):
    """

    :param img:pass the image
    :return: median blurring
    """
    src = cv2.medianBlur(img, 3)
    cv2.imshow("Median_Blurring", src)
    cv2.imwrite("/home/joemarshal/image_processing_opencv/images/Median_blurring.jpg", src)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def bilateral_blurring(img):
    """

    :param img:pass the image
    :return: bilateral blurring
    """
    src = cv2.bilateralFilter(img, 15, 50, 15)
    cv2.imwrite("/home/joemarshal/image_processing_opencv/images/Median_blurring.jpg", src)
    cv2.imshow("Bilateral_Blurring", src)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    image = cv2.imread(image_loc, cv2.IMREAD_UNCHANGED)

    guassian_blurring(image)
    median_blurring(image)
    bilateral_blurring(image)
