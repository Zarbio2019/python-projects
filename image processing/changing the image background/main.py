# Author: Zarbio Romulo

import cv2
import numpy as np

foreground = cv2.imread("giraffe.jpeg")
background = cv2.imread("safari.jpeg")

print(foreground[40, 40])
width = foreground.shape[1]
height = foreground.shape[0]
print(foreground.shape)

resized_background = cv2.resize(background, (width, height)) # to fill all the image

for i in range(width):
  for j in range(height):
    pixel = foreground[j, i] # get pixel
    # print(pixel)
    # print(type(pixel)) # numpy.ndarray
    #if list(pixel) == [28, 255, 76]: # green color, show incorrect border in green
    if np.any(pixel == [1, 255, 0]): # green color
      foreground[j, i] = resized_background[j, i] # replace pixel

cv2.imwrite('output.jpeg', foreground)
    