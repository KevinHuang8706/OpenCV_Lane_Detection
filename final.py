import cv2
import numpy as np

a=int(input(": "))
result1= cv2.VideoWriter('OpenCV_Lane_Detection/result1.mp4', cv2.VideoWriter_fourcc(*'MPEG'), 10, (1920, 1080))
def crop(img,points):
    mask = np.zeros_like(img)
    channel=img.shape[2]
    color = (255,) * channel
    cv2.fillPoly(mask, points, color)
    triangle = cv2.bitwise_and(img, mask)
    return triangle

cap= cv2.VideoCapture()
if a==1:
    cap= cv2.VideoCapture('3674.mp4')

    if cap.isOpened() == False:
        print('error loading file')
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        img = frame.copy()
        dimension = frame.shape
        height = dimension[0]
        width = dimension[1]
        points = [(455, 1080), (940, 400), (1545, 1080)]
        result = crop(img, np.array([points], np.int32), )
        gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 75, 150)
        lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 50, maxLineGap=50)
        count = 0
        if lines is not None:
            for line in lines:
                x1, y1, x2, y2 = line[0]
                # cv2.line(frame, (x1,y1),(x2,y2),(0,255,0),10)
                count = count + 1
        frame = cv2.circle(frame, (200, 820), 50, (0, 255, 255 * (59 - count) / 59), -1)
        result1.write(frame)
        if ret == True:
            cv2.imshow('video', frame)
            #print(count)
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break
        else:
            break
    cap.release()
    result1.release()
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if a==2:
    cap= cv2.VideoCapture('3686.mp4')
    result2 = cv2.VideoWriter('OpenCV_Lane_Detection/result2.mp4', cv2.VideoWriter_fourcc(*'XVID'), 10, (1920, 1080))
    if cap.isOpened() == False:
        print('error loading file')
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        img = frame.copy()
        dimension = frame.shape
        height = dimension[0]
        width = dimension[1]
        points = [(400, 1080), (750, 400), (1050, 1080)]
        result = crop(img, np.array([points], np.int32), )
        gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 75, 150)
        lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 50, maxLineGap=50)
        count = 0
        if lines is not None:
            for line in lines:
                x1, y1, x2, y2 = line[0]
                #cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 10)
                count = count + 1
        frame = cv2.circle(frame, (200, 820), 50, (0, 255, 255 * (25 - count) / 25), -1)
        result2.write(frame)
        if ret == True:
            cv2.imshow('video', frame)
            #print(count)
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break
        else:
            break
    cap.release()
    result2.release()
    cv2.waitKey(0)
    cv2.destroyAllWindows()

