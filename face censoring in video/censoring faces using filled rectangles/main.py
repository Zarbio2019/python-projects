import cv2
 
video = cv2.VideoCapture("smile.mp4")
success, frame = video.read()
 
height = frame.shape[0]
width = frame.shape[1]
 
face_cascade = cv2.CascadeClassifier('faces.xml')
output = cv2.VideoWriter('output_smile.avi', 
cv2.VideoWriter_fourcc(*'DIVX'), 30, (width, height))
 
count = 0
while success:
  faces = face_cascade.detectMultiScale(frame, 1.1, 4)
  for (x, y, w, h) in faces:
    # frame[y:y+h, x:x+w] = cv2.blur(frame[y:y+h, x:x+w], (50, 50))
    cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 255), -1)
  output.write(frame)
  success, frame = video.read()
  count += 1
  print(count)
 
output.release()