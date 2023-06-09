from bs4 import BeautifulSoup
import requests

# https://www.x-rates.com/calculator/?from=EUR&to=USD&amount=1
def get_currency(in_currency, out_currency):
  url = f'https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1'
  content = requests.get(url).text
  soup = BeautifulSoup(content, 'html.parser')
  rate = soup.find("span", class_="ccOutputRslt").get_text() # ex: 1.577551 AUD
  rate = float(rate[:-4]) # ex: 1.577551
  
  return rate

print(get_currency('EUR', 'AUD'))
