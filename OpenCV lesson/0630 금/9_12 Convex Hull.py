import cv2
import numpy as np

img = cv2.imread('/home/fenor/image/보.JPG')
img1 = img.copy()
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 120, 255, 0)
contours, hierachy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[0]
cnt = cnt.reshape((-1, 2))  # 윤곽선 배열의 형태 변경
cv2.drawContours(img, [cnt], 0, (0, 255, 0), 3)
cv2.imshow('Original Contour', img)

# contour가 Convex Hull 인지를 확인한다.
chk = cv2.isContourConvex(cnt)
 
if not chk:
   cvxhull = cv2.convexHull(cnt)
   cv2.drawContours(img1, [cvxhull], 0, (0, 255, 0), 3)
   cv2.imshow('Convex Hull', img1)

cv2.waitKey(0)
cv2.destroyAllWindows()
