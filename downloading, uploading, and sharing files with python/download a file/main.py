# Author: Zarbio Romulo

# https://filesamples.com/formats/mp3

url = "https://filesamples.com/samples/audio/mp3/Symphony%20No.6%20(1st%20movement).mp3"

import requests # get or post requests

req = requests.get(url)
content = req.content

with open('dowload.mp3', 'wb') as file: # wr = write binary mode
  file.write(content)