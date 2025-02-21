import cv2
from playsound import playsound
from plyer import notification
import numpy as np


fire_cascade = cv2.CascadeClassifier('fire_detection.xml')
print(fire_cascade.readable)
cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    fire = fire_cascade.detectMultiScale(frame, 1.2, 5)

    for (x,y,w,h) in fire:
        cv2.rectangle(frame,(x-20,y-20),(x+w+20,y+h+20),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        print("fire is detected")
        playsound('audio.mp3')
        notification.notify(
            title='fire is detected',
            message='there is fire in the location of camera',
            app_icon=None,
            timeout=10,
        )
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    
