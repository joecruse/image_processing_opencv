import numpy as np
import cv2
import matplotlib.pyplot as plt
from skimage.measure import structural_similarity as ssim


def mse(image1, image2):
    err = np.sum((image1.astype("float") - image2.astype("float")) ** 2)
    err /= float(image1.shape[0] * image2.shape[1])
    return err

def compare_images(image1, image2, title):
    m = mse(image1, image2)
    s = ssim(image1, image2)
    fig = plt.figure(title)
    plt.suptitle("MSE : %.2f, SSIM: %.2f" % (m, s))
    ax = fig.add_subplot(1, 2, 1)
    plt.imshow(image1, cmap=plt.cm.gray)
    plt.axis("off")
    ax = fig.add_subplot(1, 2, 2)
    plt.imshow(image2, cmap=plt.cm.gray)
    plt.axis("off")
    plt.show()


original = cv2.imread("/home/joemarshal/Downloads/resizedronaldo.jpg")
contrast = cv2.imread("/home/joemarshal/Downloads/contrast_ronaldo.png")
#shopped = cv2.imread("/home/joemarshal/Downloads/megingmessi&ronaldo.jpg")

original = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
contrast = cv2.cvtColor(contrast, cv2.COLOR_BGR2GRAY)
#shopped = cv2.cvtColor(shopped, cv2.COLOR_BGR2GRAY)

fig = plt.figure("Images")
images = ("Original", original), ("Contrast", contrast)

for (i, (name, image)) in enumerate(images):
    ax = fig.add_subplot(1, 2, i + 1)
    ax.set_title(name)
    plt.imshow(image, cmap=plt.cm.gray)
    plt.axis("off")


plt.show()

compare_images(original, original, "Original vs. Original")
compare_images(original, contrast, "Original vs. Contrast")
#compare_images(original, shopped, "Original vs. Photoshopped")

