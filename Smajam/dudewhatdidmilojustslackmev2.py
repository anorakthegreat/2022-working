from xml.etree.ElementTree import PI
import numpy as np
import cv2
import math

cap = cv2.VideoCapture(1)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while True:
    _, frame = cap.read()
    result = frame.copy()
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    output = frame.copy()
    #lower = np.array([155,25,0])
    #upper = np.array([179,255,255])
    # lower_blue = np.array([100,150,0])
    # upper_blue = np.array([140,255,255])
    lower = np.array([0,0,0])
    upper = np.array([255,80,110])
    #upper = np.array([255,100,100])
    #lower_blue= np.array([240,100,100])
    #upper_blue = np.array([240,100,100])
    mask = cv2.inRange(frame, lower, upper)
    result = cv2.bitwise_and(result, result, mask=mask)
    # circles = cv2.detectMul(cv2.cvtColor(result, cv2.COLOR_BGR2GRAY), cv2.HOUGH_GRADIENT, 1.2, 100)
    # if circles is not None:
    #     circles = np.round(circles[0,:]).astype("int")
    #     for (x, y, r) in circles:
    #         cv2.circle(output, (x, y), r, (0, 255, 0), 4)

    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    i = 0
    for contour in contours:
        if i == 0:
            i = 1
            continue

        if cv2.contourArea(contour) < 250:
            continue

        if cv2.arcLength(contour, True) > 1.3 * 2 * math.pi * int(math.sqrt(cv2.contourArea(contour)/math.pi)):
            continue
        approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
        if (len(approx) > 8):
            print(len(approx))
            continue 
            
        cv2.drawContours(frame, [contour], 0, (0, 255, 0), 5)
        bx, by, bw, bh = cv2.boundingRect(contour)
        cv2.rectangle(frame, (bx, by), (bx+bw,by+bh), (0, 0, 255), 2)

        M = cv2.moments(contour)
        x=0
        y=0
        if M['m00'] != 0.0:
            x = int(M['m10']/M['m00'])
            y = int(M['m01']/M['m00'])

        cv2.putText(frame, "shape", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,255), 2)        

    cv2.imshow('mask', mask)
    cv2.imshow('result', result)
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()