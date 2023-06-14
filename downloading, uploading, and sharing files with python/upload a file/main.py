# Author: Zarbio Romulo

import requests

# Upload a file to this web: https://cgi-lib.berkeley.edu/ex/fup.html

url = "https://cgi-lib.berkeley.edu/ex/fup.cgi" # use url when upload

file = open('myfile.txt', 'rb') # rb ) read binary mode

req = requests.post(url, files={"upfile":file}) # use element name input = upfile

print(req.text)