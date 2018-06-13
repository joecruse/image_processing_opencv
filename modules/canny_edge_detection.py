"""
Code for canny edge detection
"""
import cv2



if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    while 1:
        _, frame = cap.read()
        cv2.imshow("demo", frame)

        edges = cv2.Canny(frame, 100, 200)
        cv2.imshow('Edges', edges)

        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break

    cv2.destroyAllWindows()
    cap.release()
