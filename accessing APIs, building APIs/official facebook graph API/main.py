# Author: Zarbio Romulo

import requests
import json

url = "https://graph.facebook.com/v13.0/105360698771730?fields=link%2Cimages&access_token=EAAJIitQMcZBABAEZBMY7shwy9brRQzgC3WmRdST9b4oXy0t24LSZC0KEaVCvVQ4PmQwtrx0tUsv64dg5gT4FEN5UCfZAaJwSDLrqdXAjyZAJKCNHsomPBBKgtVQDdWnr301GumkMi266I3xIzPKJTcbr2ybMiwGVE9pMyZAWVyuYaKgKFegmwKtvd0geqijSCYlfgSZCrP17BnHUek8BslsJqqQ5ygMQLHLMK4HDScV1dn1jdCUBxq2ZBmkfLZB8u6HsZD"
# Facebook profile ID = "me" = 105360698771730

response = requests.get(url)
data = response.text # response.content
#print(type(data)) # dict

data = json.loads(data)
image_url = data['images'][0]['source']

image_bytes = requests.get(image_url).content

# Download image
with open('image.jpg', 'wb') as file:
  file.write(image_bytes)
