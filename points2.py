import cv2
import numpy as np



def crop(img,points):
    mask = np.zeros_like(img)
    channel=img.shape[2]
    color = (255,) * channel
    cv2.fillPoly(mask, points, color)
    triangle = cv2.bitwise_and(img,mask)
    return triangle

cap = cv2.VideoCapture('3686.mp4')

if cap.isOpened()== False:
    print('error loading file')
while cap.isOpened():
    ret,frame=cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    img=frame.copy()
    dimension=frame.shape
    height = dimension[0]
    width = dimension[1]
    points = [(400, 1080), (750, 400), (1050, 1080)]
    result= crop(img,np.array([points],np.int32),)
    gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 75, 150)
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 50, maxLineGap=50)
    count=0
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(frame, (x1,y1),(x2,y2),(0,255,0),10)
            count=count+1
    frame=cv2.circle(frame,(200,820),50,(0,255,255*(25-count)/25),-1)
    if ret == True:
        cv2.imshow('video',frame)
        print(count)
        if cv2.waitKey(50) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.waitKey(0)
cv2.destroyAllWindows()