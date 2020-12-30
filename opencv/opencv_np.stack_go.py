# import cv2
# import numpy as np

# img = cv2.imread("chessboard.jpg")
# print("img.shape = {0}".format(img.shape))
# middle = np.zeros((635, 828, 3), np.uint8)
# hstack_img = np.hstack((img, middle, img))
# print("hstack_img.shape = {0}".format(hstack_img.shape))

# last_img = np.vstack((img, hstack_img, img))
# dst = cv2.resize(last_img, (0,0), fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)
# cv2.imshow("dst", dst)
# cv2.waitKey()