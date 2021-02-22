import os
import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
video_capture =  cv2.VideoCapture(0)
while True:
    ret, frames =  video_capture.read()
    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5,
                                          minSize=(30,30), flags=cv2.CASCADE_SCALE_IMAGE)
    for (x,y,w,h) in faces:
        cv2.rectangle(frames, (x,y), (x+w, y+h), (255, 0, 0), 2)

    cv2.imshow('video',frames)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyWindow()

