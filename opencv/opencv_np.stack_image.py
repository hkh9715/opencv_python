# # vertical stack_image

# import cv2
# import numpy as np

# img = cv2.imread("chessboard.jpg")
# print("img.shape = {0}".format(img.shape))
# vstack_img = np.vstack((img, img))
# print("vstack_img.shape = {0}".format(vstack_img.shape))

# dst = cv2.resize(vstack_img, (0,0), fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)
# cv2.imshow("dst", dst)
# cv2.waitKey()


# horizontal stack_image

import cv2
import numpy as np

img = cv2.imread("chessboard.jpg")
print("img.shape = {0}".format(img.shape))
hstack_img = np.hstack((img, img))
print("hstack_img.shape = {0}".format(hstack_img.shape))

dst = cv2.resize(hstack_img, (0,0), fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)
cv2.imshow("dst", dst)
cv2.waitKey()
