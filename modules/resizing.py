import cv2



if __name__ == "__main__":
    img = cv2.imread("/home/joemarshal/image_processing_opencv/images/messi.jpg", cv2.IMREAD_REDUCED_COLOR_4)
    width = int(input())
    # give the input width and height
    height = int(input())
    r = width / img.shape[1]
    dim = (height, int(img.shape[0] * r))
    resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    cv2.imshow("resize", resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
