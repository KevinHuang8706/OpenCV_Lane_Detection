import cv2
import numpy as np
from matplotlib import pyplot as plt
img=cv2.imread('kang240.jpg')
img=cv2.circle(img,(490,1080),20,(0,255,0),-1)
img=cv2.circle(img,(1000,1080),20,(0,255,0),-1)
img=cv2.circle(img,(940,400),20,(255,255,0),-1)
points=np.array([[875,400],[500,1080],[1000,1080]],np.int32)
img=cv2.polylines(img,[points],True,(0,255,0),10)
plt.imshow(img)
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
