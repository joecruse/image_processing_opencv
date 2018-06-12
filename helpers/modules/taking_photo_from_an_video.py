import cv2
import numpy as np

if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    while True:
        _, frame = cap.read()
        cv2.imshow("frame", frame)
        key = cv2.waitKey(0)
        if key == 27:
            break
    cv2.imwrite("/home/frame.jpg", frame)
    cap.release()
    cv2.destroyAllWindows()
