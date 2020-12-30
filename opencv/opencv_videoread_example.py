import numpy as np
import cv2

cap = cv2.VideoCapture('test2.mp4')
print(cap.get(3), cap.get(4))

while(cap.isOpened()):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    resize = cv2.resize(gray, (320, 240))
    cv2.imshow('frame', resize)
    key = cv2.waitKey(100)
    if key == ord('q'):
        break
    if key == ord('p'):
        cv2.waitKey(-1) #wait until any key is pressed
cap.release()
cv2.destroyAllWindows()

# 256X768