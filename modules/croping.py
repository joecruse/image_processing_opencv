"""
Code to crop an image
"""
import cv2


if __name__ == "__main__":
    img = cv2.imread("/home/joemarshal/image_processing_opencv/images/ronaldo.jpg", cv2.IMREAD_COLOR)
    cropped = img[70:250, 100:540]
    cv2.imshow("croping", cropped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
