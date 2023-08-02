import numpy as np
import cv2

cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier('/home/fenor/image/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('/home/fenor/image/haarcascade_eye.xml')

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        img = cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

        # 얼굴 영역에서 윤곽선(contour)을 찾습니다.
        contours, _ = cv2.findContours(roi_gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        # 얼굴 영역에 윤곽선을 그립니다.
        cv2.drawContours(roi_color, contours, -1, (0, 0, 255), 2)
        
        # 윤곽선에 대한 볼록 다각형(convex hull)을 찾습니다.
        hulls = [cv2.convexHull(contour) for contour in contours]
        
        # 얼굴 영역에 볼록 다각형을 그립니다.
        cv2.drawContours(roi_color, hulls, -1, (255, 0, 255), 2)

    cv2.imshow('Detect', img)
    if cv2.waitKey(10) == 27:
        break
    
cap.release()
cv2.destroyAllWindows()
