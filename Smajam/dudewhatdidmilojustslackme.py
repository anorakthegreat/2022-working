import numpy as np
import cv2

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

image = cv2.imread("ball.jpg")
result = image.copy()
image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
# lower = np.array([155,25,0])
# upper = np.array([179,255,255])
lower = np.array([100,150,50])
upper = np.array([150,255,255])
mask = cv2.inRange(image, lower, upper)
result = cv2.bitwise_and(result, result, mask=mask)

# cv2.imshow('mask', mask)
cv2.imshow('result', result)
cv2.waitKey()
