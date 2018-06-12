import cv2
import numpy as np
from image_reader_1 import show_image

if __name__ == "__main":
   cap = cv2.VideoCapture(0)
   while True:
      ret, frame = cap.read()
      cv2.imshow("frame", frame)
      cv2.line(frame, (500, 400), (640, 480), (0, 255, 0), 3)

      key = cv2.waitKey(60)

      if key == 27:
         break
      cap.release()
      cv2.destroyAllWindows()