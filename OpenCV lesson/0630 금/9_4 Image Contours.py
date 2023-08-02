#Filename : contour.py 

import numpy as np 
import cv2 
 
img = cv2.imread('/home/fenor/image/ci.png') 
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
ret,thresh = cv2.threshold(imgray,200,255, cv2.THRESH_BINARY_INV) 
# 이미지에서 contour를 탐색한다
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE ,cv2.CHAIN_APPROX_NONE) 

# 탐색된 contour를 원본 이미지에 그린다
cv2.drawContours(img, contours, -1, (0,0,255), 1) 

cv2.imshow('origin', img) 
cv2.imshow('gray', imgray) 
cv2.imshow('threshold', thresh) 

cv2.waitKey(0) 
cv2.destroyAllWindows() 
