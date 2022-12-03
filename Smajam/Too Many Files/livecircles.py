import numpy as np
import cv2 as cv
cap = cv.VideoCapture(0)
cap.set(cv.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 720)
    
while True:
    _, img = cap.read()
    #img = frame.copy()
    img = cv.medianBlur(img,5)
    cimg = cv.cvtColor(img,cv.COLOR_GRAY2BGR)
    circles = cv.HoughCircles(img,cv.HOUGH_GRADIENT,1,20,
                            param1=100,param2=100,minRadius=0,maxRadius=0)
    circles = np.uint16(np.around(circles))
    for i in circles[0,:]:
    # draw the outer circle
        cv.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
        cv.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
    cv.imshow('detected circles',cimg)
    key = cv.waitKey(1)
    if key == 27:
        break

cap.release()
cv.destroyAllWindows()