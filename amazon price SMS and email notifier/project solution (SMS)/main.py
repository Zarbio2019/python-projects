# Author: Zarbio Romulo

from selenium import webdriver # to scrape the web
from twilio.rest import Client # to send SMS
import time

# scrape the web to get the value of the price
def get_driver():
# Set options to make browsing easier
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")

  driver = webdriver.Chrome(options=options)
  driver.get("https://www.amazon.com/PF-WaterWorks-PF0989-Disposal-Installation/dp/B078H38Q1M/")
  return driver

def main():
  driver = get_driver()
  # xpath was taken in Chrome by right-clicking
  # over <span aria-hidden="true">$15.12</span>
  # and then Copy -> xpath
  element = driver.find_element(by="xpath", value='//*[@id="corePrice_desktop"]/div/table/tbody/tr/td[2]/span[1]/span[2]')
  # print('element', element.text)
  return element.text # get value scrape from web

#print(main()) # ex: $16.33
  
# delete the $ value (ex: $16.33)
def clean_price(raw):
  return float(raw.replace('$', ''))

#raw_price = main()
#print(clean_price(raw_price)) # ex: 16.33

# send SMS
account_sid = 'AC2c8f548726a631d1c284c6dbf2416af2'
auth_token = 'd0ec70ee1d61bb5cd610edf87567c35f'
client = Client(account_sid, auth_token)

raw_price = main()
price = clean_price(raw_price)

prices = [price] # list of prices (old and last)

while True:
  time.sleep(5)
  raw_price = main()
  price = clean_price(raw_price)
  prices.append(price) # add last price
  print(prices) # 2 prices

  if prices[-1] < prices[-2]: # compare old price with last price
    message = client.messages.create(
                  body=f"The price has just dropped to ${price}. Hurry up!",
                  from_='+00000',
                  to='+00000'
                  )
  del prices[-2] # delete old price
  