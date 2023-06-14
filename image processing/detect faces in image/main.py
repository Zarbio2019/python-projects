# Author: Zarbio Romulo

import cv2

image = cv2.imread('humans.jpeg', 1)
face_cascade = cv2.CascadeClassifier('faces.xml')

faces = face_cascade.detectMultiScale(image, 1.1, 4) # for faces near of far
# 1.1 = scale factor, 4 = minimum neighbors
# cv find a face with different scales
print(faces) # list of arrays

for (x, y, w, h) in faces: # x, y, weight, height
  cv2.rectangle(image, (x, y), (x+w, y+h), (255, 255, 255), 4) # 4 = wide of rectangle

cv2.imwrite('human_faces.jpeg', image)
