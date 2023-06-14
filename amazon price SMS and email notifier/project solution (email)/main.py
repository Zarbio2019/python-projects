# Author: Zarbio Romulo

from selenium import webdriver
import yagmail
import time
import os

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
  return element.text

def clean_price(raw):
  return float(raw.replace('$', ''))

# send email
sender = 'app7flask@gmail.com'
receiver = '2jjnkjca@10mail.tk'

raw_price = main()
price = clean_price(raw_price)

prices = [price]


while True:
  time.sleep(5)
  raw_price = main()
  price = clean_price(raw_price)
  prices.append(price)
  print(prices)

  if prices[-1] < prices[-2]:
    subject = f"The price has just dropped to ${price}. Hurry up!"
    contents = f"""
    Hey, I just noticed the price dropped to ${price}
    """
    yag = yagmail.SMTP(user=sender, password=os.getenv('PASSWORD'))
    yag.send(to=receiver, subject=subject, contents=contents)

    # (optional) Print out a message that email was sent
    print("Email Sent!")
  del prices[-2]
