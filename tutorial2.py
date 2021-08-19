import cv2
import random

img = cv2.imread('person.jpeg', -1)

# change color
# for i in range(100):
#     for j in range(img.shape[1]):
#         img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

# copy part of img

tag = img[400:600, 400:700]
img[100:300, 200:500] = tag


cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
