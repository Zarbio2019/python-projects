# Author: Zarbio Romulo

import requests

def get_weather(city, units='metric', api_key='26631f0f41b95fb9f5ac0df9a8f43c92'):
  url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units={units}"
  r = requests.get(url)
  content = r.json()
  
  # write in file
  with open('data.txt', 'a') as file: # a = append
    for dicty in content['list']:
      #print(dicty['dt_txt'])
      file.write(f"{dicty['dt_txt']}, {dicty['main']['temp']}, {dicty['weather'][0]['description']}\n")

print(get_weather(city='Washington'))
