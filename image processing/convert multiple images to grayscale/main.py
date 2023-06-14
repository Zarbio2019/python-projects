# Author: Zarbio Romulo

import os
import cv2

images = os.listdir('images')
print(images)

for image in images:
  print(image)
  gray = cv2.imread(f'images/{image}', 0)
  print(gray)
  cv2.imwrite(f'grayimages/gray-{image}', gray)