import cv2
import numpy as np
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('output.MOV', fourcc, 20.0, (640, 480))
if __name__ =="__main__":
    video = cv2.VideoCapture(0)
    while True:
        _, frame = video.read()
        cv2.imshow("frame", frame)
        key = cv2.waitKey(65)
        cv2.line(frame, (500, 400), (640, 480), (0, 255, 0), 3)
        cv2.putText(frame, "EDITING IN A VIDEO!", (105, 105), cv2.FONT_HERSHEY_COMPLEX, .7, (225, 0, 0))
        out.write(frame)
        if key == 27:
            break
    out.release()
    video.release()
    cv2.destroyAllWindows()