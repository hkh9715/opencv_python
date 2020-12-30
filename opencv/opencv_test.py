import cv2
import numpy as np

# print(cv2.__version__)
# print(cv2.__file__)

a = cv2.imread(".\Back_View.jpg")
print(a.shape[1])