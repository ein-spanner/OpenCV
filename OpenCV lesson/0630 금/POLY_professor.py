import cv2
import numpy as np

img = cv2.imread("/home/fenor/image/POLY.jpg")
img1 = img.copy()

imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(imgray, 200, 255, cv2.THRESH_BINARY_INV)
contours, h = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

color = [(0,0,0), (255,255,255), (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0,255,255), (255, 0, 255), (128, 128, 0), (0, 128, 128), (128, 0, 128)]

num = 1
for con in contours:
    epsilon = 0.02 * cv2.arcLength(con, True)
    approx = cv2.approxPolyDP(con, epsilon, True)

    num = num + 1

    pnum = 0
    for p in approx:
        pnum = pnum + 1

    cv2.drawContours(img, [con], -1, color[pnum], -1)

cv2.imshow("img", img)

cv2.waitKey(0)
cv2.destroyAllWindows()