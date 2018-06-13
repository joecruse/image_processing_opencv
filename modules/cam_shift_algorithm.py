import cv2
import numpy as np


if __name__ == "__main__":
    img = cv2.imread("/home/joemarshal/image_processing_opencv/images/phone61.png")
    roi = img[0:245, 0:245]
    x = 0
    y = 0
    height = 240
    width = 240
    cv2.imshow("roi", roi)


    hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
    roi_hist = cv2.calcHist([hsv_roi], [0], None, [180], [0, 180])

    cap = cv2.VideoCapture(0)

    term_criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)

    while True:
        _, frame = cap.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)
        x1 = 100
        y1 = 150
        height1 = 150
        width1 = 150
        ret, track_window = cv2.CamShift(mask, (x1, y1, width1, height1), term_criteria)

        pts = cv2.boxPoints(ret)
        pts = np.int0(pts)
        cv2.polylines(frame, [pts], True, (255, 0, 0), 2)

        cv2.imshow("mask", mask)
        cv2.imshow("Frame", frame)

        key = cv2.waitKey(1)
        if key == 27:
            break

    cap.release()
    cv2.destroyAllWindows()
