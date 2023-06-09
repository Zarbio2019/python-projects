import requests
import json

url = 'https://api.languagetool.org/v2/check'
data = {
    'text': 'Tis is a nixe day!',
    'language':'auto'
}

response = requests.post(url, data=data) 
# post = server process data
# get = server get data

result = json.loads(response.text) # convert string to dictionary
print(result)
