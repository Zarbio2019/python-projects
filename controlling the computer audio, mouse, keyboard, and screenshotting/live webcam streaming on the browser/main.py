import cv2 # command to install: pip install opencv-python
from flask import Flask, render_template, Response # command to install: pip install flask

video = cv2.VideoCapture(1) # 1 for laptop camera

# generator to return frames from video
# generator (is not a function), because use a yield to return statement
def get_frame():
  while True:
      success, frame = video.read()
      sc, encoded_image = cv2.imencode('.jpg', frame) # get a frame from video
      frame = encoded_image.tobytes()
      yield (b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + frame + b'\r\n') # build the image: header + frame

# build the web app  
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/vide_feed_url')
def video_feed(): # same function from index.html
    return Response(get_frame(), mimetype='multipart/x-mixed-replace; boundary=frame')

# if you want to access the web app from the local computer
if __name__ == "__main__":
  app.run(debug=True)
  
# if you want to access the web app from another computer on the same network
if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0', port=5001)
# you need to find the IP address of the local computer
# in Windows: CMD, ipconfig, item IPv4 Address
  