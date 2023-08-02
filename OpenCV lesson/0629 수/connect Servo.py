import numpy as np
import cv2
from gpiozero import AngularServo
from time import sleep

servo = AngularServo(17, min_angle=-90, max_angle=90)

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
            # Servo 모터 각도 변경
            if ex + ew/2 < w/2:
                servo.angle = -90
            else:
                servo.angle = 90

    cv2.imshow('Detect', frame)
    if cv2.waitKey(10) == 27:
        break

cap.release()
cv2.destroyAllWindows()
