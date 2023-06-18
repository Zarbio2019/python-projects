# Author: Zarbio Romulo

# request info of package:
# from sunnyday import Weather
# help(Weather)
#
# weather1 = Weather(apikey = "26631f0f41b95fb9f5ac0df9a8f43c92", city = "Madrid")
# weather1.next_12h()
# weather1.next_12h_simplified()
# print(weather1.next_12h_simplified())

import requests

# sample to get weather data:
#url = "http://api.openweathermap.org/data/2.5/forecast?q=Madrid&APPID=26631f0f41b95fb9f5ac0df9a8f43c92&units=imperial"
#r = requests.get(url)
#print(r.text)
#print(r.json)

class Weather:
  """Creates a Weather object getting an apikey as input
  and either a city name or lat and lon coordinates.
  
  Package use example:
  
  # Create a weather object using a city name:
  # The api key below is not guarantteed to work.
  # Get your own apikey from https://openweathermap.org
  # And wait a couple of hours for the apikey to be activated
  
  >>> weather1 = Weather(apikey = "26631f0f41b95fb9f5ac0df9a8f43c92", city = "Madrid")
  
  # Using latitude and longitude coordinates
  >>> weather2 = Weather(apikey = "26631f0f41b95fb9f5ac0df9a8f43c92", lat = 41.1, lon = -4.1)
  
  # Get complete weather data for the next 12 hours:
  >>> weather1.next_12h()
  
  # Simplified data for the next 12 hours:
  >>> weather1.next12h_simplified()
  
  Sample url to get sky condition icons (from https://openweathermap.org/weather-conditions):
  http://openweathermap.org/img/wn/10d@2x.png
  
  """
  def __init__(self, apikey, city=None, lat=None, lon=None):
  
    if city:
        url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&APPID={apikey}&units=imperial"
        r = requests.get(url)
        self.data = r.json()
    else lat and lon:
        url = f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&APPID={apikey}&units=imperial"
        r = requests.get(url)
        self.data = r.json()
    else:
      raise TypeError("provide either a city or lat and lon arguments")
      
    if self.data["cod"] != "200":
      raise ValueError(self.data["message"])
      
  def next_12h(self):
    """Returns 3-hour data for the next 12 hours as a dict.
    """
    return self.data['list'][:4]
    
  def next_12h_simplified(self):
  
    simple_data = []
    for dicty in self.data['list'][:4]:
      simple_data.append((dicty['dt_txt'], dicty['main']['temp'], dicty['weather'][0]['description'], dicty['weather'][0]['icon']))
    return simple_data
    #return(self.data['list'][0]['dt_txt'], self.data['list'][0]['main']['temp'], self.data['list'][0]['weather'][0])['description'])

    #sky conditions: dicty['weather'][0]['icon']
    
#weather = Weather(apikey = "26631f0f41b95fb9f5ac0df9a8f43c92", city = "Valencia")
#weather = Weather(apikey = "26631f0f41b95fb9f5ac0df9a8f43c92", lat = 4.1, lon = 3.2)
#weather = Weather(apikey = "26631f0f41b95fb9f5ac0df9a8f43c92", city = "Madrid", lat = 4.1, lon = 3.2)
#print(weather.data)
#print(weather.next_12h())

# test of package:
#import sunnyday
#weather1 = sunnyday.Weather(apikey = "26631f0f41b95fb9f5ac0df9a8f43c92", city = "Nairobi")
#print(weather1.next_12h())
#print(weather1.next_12h_simplified())

#weather1 = sunnyday.Weather(apikey = "26631f0f41b95fb9f5ac0df9a8f43c92", lat = 10, lon = -20)
#print(weather1.next_12h_simplified())
#print(weather1.next_12h())
#help(sunnyday.Weather)

#weather1 = sunnyday.Weather(apikey = "26631f0f41b95fb9f5ac0df9a8f43c92", lat = 10, lon = -20)
#weather1.next_12h_simplified()[0][-1] # return '04d'
