#Filename : Convexity Defects.py

import cv2
import numpy as np

img = cv2.imread('/home/fenor/image/star.png')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 120,255,0) 
contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

# original contour를 얻은 후 그린다.
cv2.drawContours(img, contours, -1, (0,255,0), 2)
cnt = contours[0]
 
# convex hull을 얻는다.
hull = cv2.convexHull(cnt,returnPoints = False)
# convexity defects를 구한다.
defects = cv2.convexityDefects(cnt,hull)

for i in range(defects.shape[0]):
   s,e,f,d = defects[i,0]
   start = tuple(cnt[s][0])
   end = tuple(cnt[e][0])
   far = tuple(cnt[f][0])
   cv2.line(img, start, end,[255,0,0], 2)
   cv2.circle(img, far, 3, [0,0,255], -1)

cv2.imshow('img',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
