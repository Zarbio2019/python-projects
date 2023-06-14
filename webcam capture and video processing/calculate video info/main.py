# Author: Zarbio Romulo

import cv2

video = cv2.VideoCapture("video.mp4")

width = video.get(cv2.CAP_PROP_FRAME_WIDTH)
height = video.get(cv2.CAP_PROP_FRAME_HEIGHT)
nr_frames = video.get(cv2.CAP_PROP_FRAME_COUNT) # number of frames
fps = video.get(cv2.CAP_PROP_FPS) # frames per second

print(width, height, nr_frames, fps)