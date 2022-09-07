import numpy as np
import cv2

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while True:
    _, frame = cap.read()
    result = frame.copy()
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower = np.array([155,25,0])
    upper = np.array([179,255,255])
    #lower_blue = np.array([100,150,0])
    #upper_blue = np.array([140,255,255])
    lower_blue= np.array([240,100,100])
    upper_blue = np.array([240,100,100])
    mask = cv2.inRange(frame, lower_blue, upper_blue)
    result = cv2.bitwise_and(result, result, mask=mask)
    cv2.imshow('mask', mask)
    cv2.imshow('result', result)
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()