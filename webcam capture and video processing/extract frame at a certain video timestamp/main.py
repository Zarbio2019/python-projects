# Author: Zarbio Romulo

import cv2

video = cv2.VideoCapture("video.mp4")

nr_frames = video.get(cv2.CAP_PROP_FRAME_COUNT)
fps = video.get(cv2.CAP_PROP_FPS)

#timestamp = '00:00:02.75' # 1 second = 30 frames
timestamp = input('Enter timestamp in hh:mm:ss format: ') # 00:00:01.88 

timestamp_list = timestamp.split(':')
hh, mm, ss = timestamp_list
#print(timestamp_list)

timestamp_list_floats = [float(i) for i in timestamp_list]
hours, minutes, seconds = timestamp_list_floats
print(hours, minutes, seconds)

# get the number of a frame in a time stamp
frame_nr = hours * 3600 * fps + minutes * 60 * fps + seconds * fps

video.set(1, frame_nr)
succes, frame = video.read()
cv2.imwrite(f'Frame at {hh}:{mm}:{ss}.jpg', frame)
print(width, height, nr_frames, fps)