"""
Here you will see how to read the video from a file
"""
import cv2


def video_reader(path):
    """

    :param path: takes the path value of the video
    :return: returns the video to display
    """
    cap = cv2.VideoCapture(path)
    while True:
        ret, frame = cap.read()
        # here this loops helps in running the file for infinite times
        if not ret:
            cap = cv2.VideoCapture(path)
            continue

        cv2.imshow("video", frame)
        key = cv2.waitKey(1)
        if key == 27:
            break
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    path1 = "/home/joemarshal/image_processing/videos/road_car_view.mp4"
    video_reader(path1)
