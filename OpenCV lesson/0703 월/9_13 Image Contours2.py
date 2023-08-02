# origin, gray, threshold, convex hull, convexity defects

import numpy as np 
import cv2 
 
img = cv2.imread('/home/fenor/image/korea.jpg') 
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
ret, thresh = cv2.threshold(imgray, 200, 255, cv2.THRESH_BINARY_INV) 
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# origin 이미지
cv2.imshow('origin', img) 

# gray 이미지
cv2.imshow('gray', imgray) 

# threshold 이미지
cv2.imshow('threshold', thresh) 

# convex hull 이미지
cv2.drawContours(img, contours, -1, (0, 255, 0), 2)
cv2.imshow('convex hull', img) 

# convexity defects 이미지
cv2.drawContours(img, contours, -1, (0, 0, 255), 1) 
cnt = contours[0]
hull = cv2.convexHull(cnt, returnPoints=False)
defects = cv2.convexityDefects(cnt, hull)

for i in range(defects.shape[0]):
    s, e, f, d = defects[i, 0]
    start = tuple(cnt[s][0])
    end = tuple(cnt[e][0])
    far = tuple(cnt[f][0])
    cv2.line(img, start, end, [255, 0, 0], 2)
    cv2.circle(img, far, 3, [0, 0, 255], -1)

cv2.imshow('convexity defects', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
