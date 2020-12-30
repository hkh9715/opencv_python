import cv2
import numpy as np

cap = cv2.VideoCapture("test2.mp4") 
print(cap.get(3), cap.get(4)) #(1280, 720)

while(cap.isOpened()):
    ret, frame = cap.read()
    hstack_video = np.hstack((frame, frame))
    print("hstack_video.shape = {0}".format(hstack_video.shape)) #(720, 2560)
    dst = cv2.resize(hstack_video, (0,0), fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)
    cv2.imshow('dst', dst)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    if key == ord('p'):
        cv2.waitKey(-1) # wait until any key is pressed


cap.release()
cv2.destroyAllWindows()