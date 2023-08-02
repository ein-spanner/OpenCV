#Filename : approx.py 

import numpy as np 
import cv2 
 
# 400 x 300의 칼라 영역을 생성한다
img = np.zeros((300,400, 3), np.uint8) 

# White 칼라의 직사각형을 그린다.
img1 = cv2.rectangle(img,(50,100),(350,200),(255,255,255),-1) 
# 사각형을 복사한다.
img2 = img1.copy() 
# 이미지를 그레이스케일로 변환한다.
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
 
# CHAIN_APPROX_NONE 근사법으로 Contour를 찾는다.
contours1, hierarchy = cv2.findContours(imgray,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE) 
# CHAIN_APPROX_SIMPLE 근사법으로 Contour를 찾는다.
contours2, hierarchy = cv2.findContours(imgray,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) 

print('APPROX_NONE : ', contours1[0].shape) 
print('APPROX_SIMPLE : ', contours2[0].shape) 

# 이미지에 Contour를 그린다.
for i in contours1[0]:
    cv2.circle(img1, (i[0][0], i[0][1]), 3, (0, 0, 255), -1) 

for i in contours2[0]:
    cv2.circle(img2, (i[0][0], i[0][1]), 3, (0, 0, 255), -1) 

cv2.imshow('APPROX_NONE', img1) 
cv2.imshow('APPROX_SIMPLE', img2) 

cv2.waitKey(0) 
cv2.destroyAllWindows() 
