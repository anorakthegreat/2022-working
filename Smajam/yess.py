import cv2
img = cv2.imread("apple.jpg")

print(img)

cv2.imshow("Img", img)

cv2.waitKey(0)