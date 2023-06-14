# Author: Zarbio Romulo

import cv2 # computer vision

color = cv2.imread('galaxy.jpeg', 0) # 0 = grey, 1 = color
print(color) # print number RGB
print(color.ndim) # dimension of color, 3 = RGB
print(type(color)) # numpy.ndarray
cv2.imwrite('galaxy-gray.jpeg', color)