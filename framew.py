import cv2
import numpy as np
from matplotlib import pyplot as plt

cap = cv2.VideoCapture('3686.mp4')
i = 0
while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break
    cv2.imwrite('kang' + str(i) + '.jpg', frame)
    i += 1

cv2.waitKey(0)
cv2.destroyAllWindows()