import numpy as np
import cv2
from helpers.image_reader import image_reader, show_image


def eroding_image(img):
    kernel = np.ones((5, 5), np.uint8)
    result_eroding_image = cv2.erode(img, kernel, iterations=1)
    return result_eroding_image

def dilating_image(img):
    kernel = np.ones((5, 5), np.uint8)
    result_dilating_image = cv2.dilate(img, kernel, iterations=2)
    return result_dilating_image

def opening_image_morphology(img):
    kernel = np.ones((5, 5), np.uint8)
    result_opening_image_morphology = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    return result_opening_image_morphology

def closing_image_morphology(img):
    kernel = np.ones((5, 5), np.uint8)
    result_closing_image_morphology = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    return result_closing_image_morphology

def morphological_gradient(img):
    kernel = np.ones((5, 5), np.uint8)
    result_morphological_gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
    return result_morphological_gradient

def morphological_tophat(img):
    kernel = np.ones((5, 5), np.uint8)
    result_morphological_tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
    return result_morphological_tophat

def morphological_blackhat(img):
    kernel = np.ones((5, 5), np.uint8)
    result_morphological_blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
    return result_morphological_blackhat




if __name__ == "__main__":
    im = "/home/joemarshal/Downloads/watershed_coins_01.jpg"
    mode = 0
    img = image_reader(im, mode)
    show_image(img)
    erotion = eroding_image(img)
    dilation = dilating_image(img)
    opening_image = opening_image_morphology(img)
    closing_image = closing_image_morphology(img)
    gradient = morphological_gradient(img)
    tophat = morphological_tophat(img)
    blackhat = morphological_blackhat(img)
    show_image(erotion)
    show_image(dilation)
    show_image(opening_image)
    show_image(closing_image)
    show_image(gradient)
    show_image(tophat)
    show_image(blackhat)