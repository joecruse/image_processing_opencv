import cv2

from helpers.image_reader import image_reader, show_image


im = "/home/joemarshal/Downloads/himan.png"
mode = -1
img = image_reader(im, mode)

# print(img.shape)

height, width, *no_of_channels = img.shape

print(height, width, no_of_channels)

for h in range(height):
    for w in range(width):
        k = img[h][w]
        k = k[:3]
        img1[h][w] = k

show_image(img)

cv2.imwrite("trying.png", img)



