import cv2

img = cv2.imread('person.jpeg', 0)

# resize img
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

# rotate img
img = cv2.rotate(img, cv2.cv2.ROTATE_180)

# save img
cv2.imwrite("new_img.jpeg", img)

# display image
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()