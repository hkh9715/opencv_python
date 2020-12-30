import cv2
import numpy as np
import matplotlib.pyplot as plt

# image = cv2.imread('./Around-View-Monitoring-AVM/dataset/Front_View.jpg')
image1 = cv2.imread('./Around-View-Monitoring-AVM/dataset/Undistorted_Front_View.jpg')

# print(image)
# canny2 = cv2.Canny(blur, 50, 300)
# cv2.imshow('lane_image', lane_image)
# plt.imshow(image)
plt.imshow(image1)
# cv2.imshow('canny2', canny2)
plt.show()

# [100, height], [400, 200], [800, height]