# https://daeunginfo.blogspot.com/2019/11/opencv-python-np-vstack-hstack.html?m=1

#vertical stack

# import numpy as np

# arr1 = np.array([[1, 1, 1]])
# arr2 = np.array([[3, 3, 3]])
# arr3 = np.array([[6, 6 ,6], [6, 6, 6]])
# print("{0}, arr1.shape = {1}".format(arr1, arr1.shape))
# print("{0}, arr2.shape = {1}".format(arr2, arr2.shape))
# print("{0}, arr3.shape = {1}".format(arr3, arr3.shape))

# vstack_arr1 = np.vstack((arr1, arr2))
# print("{0}, vstack_arr1.shape = {1}".format(vstack_arr1, vstack_arr1.shape))

# vstack_arr2 = np.vstack((arr1, arr2, arr3))
# print("{0}, vstack_arr2.shape = {1}".format(vstack_arr2, vstack_arr2.shape))


#horizontal stack

import numpy as np

arr1 = np.array([[1], [1], [1]])
arr2 = np.array([[3], [3], [3]])
arr3 = np.array([[6, 6], [6, 6], [6, 6]])
print("{0}, arr1.shape = {1}".format(arr1, arr1.shape))
print("{0}, arr2.shape = {1}".format(arr2, arr2.shape))
print("{0}, arr3.shape = {1}".format(arr3, arr3.shape))

hstack_arr1 = np.hstack((arr1, arr2))
print("{0}, hstack_arr1.shape = {1}".format(hstack_arr1, hstack_arr1.shape))

hstack_arr2 = np.hstack((arr1, arr2, arr3))
print("{0}, hstack_arr2.shape = {1}".format(hstack_arr2, hstack_arr2.shape))
