# Author: Zarbio Romulo

import cv2

video = cv2.VideoCapture("video.mp4")
success, frame = video.read()
#print(video.read()) # return tuple

count = 1
while success:
  cv2.imwrite(f'images/{count}.jpg', frame)
  success, frame = video.read()
  count += 1