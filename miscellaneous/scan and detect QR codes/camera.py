import cv2
import webbrowser

video = cv2.VideoCapture(1) # 1 for camera laptop
success, frame = video.read()
detector = cv2.QRCodeDetector()

while success:
  #cv2.imshow('frame', frame)
  
  url, coords, pixels = detector.detectAndDecode(frame)
  if url: # open url one time
    webbrowser.open(url)
    break
  
  cv2.imshow('frame', frame)
  
  if cv2.waitKey(1) == ord('q'): # press 'q' key to exit
     break
  
  success, frame = video.read()

video.release()
cv2.destroyAllWindows()
