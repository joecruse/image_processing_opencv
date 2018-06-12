import cv2

class CompareImage(object):

    def __init__(self, image_1_path, image_2_path):
        self.minimum_commutative_image_diff = 1
        self.image_1_path = image_1_path
        self.image_2_path = image_2_path

    def compare_image(self):
         image1 = cv2.imread(self.image_1_path, 0)
         image2 = cv2.imread(self.image_2_path, 0)
         commutative_self_diffrence = self.get_image_difference(image1, image2)


         if commutative_self_diffrence < self.minimum_commutative_image_diff:
             print("Matched\n")
             return commutative_self_diffrence
         return 1000

    def get_image_difference(self, image_1, image_2):
        first_image_hist = cv2.calcHist([image_1], [0], None, [256], [0, 256])
        second_image_hist = cv2.calcHist([image_2], [0], None, [256], [0, 256])

        img_hist_diff = cv2.compareHist(first_image_hist, second_image_hist, cv2.HISTCMP_BHATTACHARYYA)
        img_template_probability_match = \
        cv2.matchTemplate(first_image_hist, second_image_hist, cv2.TM_CCOEFF_NORMED)[0][0]
        img_template_diff = 1 - img_template_probability_match
        commutative_image_diff = (img_hist_diff / 10) + img_template_diff
        return commutative_image_diff
if __name__ =="__main__":
    compare_image = CompareImage("/home/joemarshal/Downloads/contrast_ronaldo.jpg", "/home/joemarshal/Downloads/contrased_ronaldo.jpg")
    image_difference = compare_image.compare_image()
    print(image_difference)


