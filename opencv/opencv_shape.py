# it makes me confused. ORDER... (width, height)? (height, width)? 
# so I write examples for better understanding.

#img.shape = (height, width, 3)
import cv2
import numpy as np

img = cv2.imread('context-based parking slot detection\\test\\image\\180109_00_002039.jpg')
print(img.shape)
cv2.imshow('display', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#np.shape = (row, column)
# arr1 = np.array([[1], [1], [1]])
# arr2 = np.array([[3], [3], [3]])
# arr3 = np.array([[6, 6], [6, 6], [6, 6]])
# print("{0}, arr1.shape = {1}".format(arr1, arr1.shape))
# print("{0}, arr2.shape = {1}".format(arr2, arr2.shape))
# print("{0}, arr3.shape = {1}".format(arr3, arr3.shape))

# #size = ()
# #continued...
# img = cv2.imread('.\chessboard.jpg')
