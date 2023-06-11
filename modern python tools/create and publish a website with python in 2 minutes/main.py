from flask import Flask

app = Flask(__name__) # create an object instance using Flask class

@app.route('/') # / = homepage
def home():
  return "Welcome to my website!"

app.run(host='0.0.0.0')