#How to make video slow

import cv2
import time

video = cv2.VideoCapture("./Around-View-Monitoring-AVM/dataset/front_camera.avi")


# prev_time = 0
# FPS = 29

# while True:

#     ret, frame = video.read()
    
#     current_time = time.time() - prev_time

#     if (ret is True) and (current_time > 1./ FPS) :
    	
#         prev_time = time.time()
        
#         cv2.imshow('video', frame)
    	
#         if cv2.waitKey(10) == ord('q'):
#             break