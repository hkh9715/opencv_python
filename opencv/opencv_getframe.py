# -*- coding: utf-8 -*-
__author__ = 'Seran'
 
import cv2
 
# 영상의 의미지를 연속적으로 캡쳐할 수 있게 하는 class
vidcap = cv2.VideoCapture('test2.mp4')
 
count = 0

# get() 함수를 이용하여 전체 프레임 중 1/100의 프레임만 가져와 저장
while(vidcap.isOpened()):
    ret, image = vidcap.read()
    resize = cv2.resize(image, (320, 240))
    cv2.imshow('frame', resize)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    if key == ord('p'):
        cv2.waitKey(-1) #wait until any key is pressed

    if(int(vidcap.get(1)) % 100 == 0):

        print('Saved frame number : ' + str(int(vidcap.get(1))))
        cv2.imwrite("image/frame%d.jpg" % count, resize)
        print('Saved frame%d.jpg' % count)
        count += 1

vidcap.release()
cv2.destroyAllWindows()


# 출처: https://shilan.tistory.com/entry/Python을-이용하여-동영상으로부터-이미지추출-Pythonv27-OpenCV-Windows [끄적끄적]