import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    
    cv2.imshow("image", img)
    if cv2.waitKey(1) == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()