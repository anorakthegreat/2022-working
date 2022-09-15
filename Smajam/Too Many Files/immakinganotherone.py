import numpy as np
import cv2 as cv
img = cv.imread('ball.jpg', 0)
cv.imshow('original',img)

#img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#img = cv.GaussianBlur(img, (22, 22), 0)
img = cv.GaussianBlur(img,(301,301),cv.BORDER_DEFAULT)

cv.imshow('blur',img)
#img = cv.medianBlur(img,5)
#cv.imshow('median blur',img)

cv.waitKey(0)
cv.destroyAllWindows()