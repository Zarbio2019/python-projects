from selenium import webdriver
import os
import smtplib
from email.mime.text import MIMEText

def get_driver():
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")

  driver = webdriver.Chrome(options=options)
  driver.get("https://zse.hr/en/indeks-366/365?isin=HRZB00ICBEX6")
  return driver

def percentage_change(driver):
  element = driver.find_element(by="xpath", value="//*[@id='app_indeks']/section[1]/div/div/div[2]/span[2]")
  value = element.text.replace(" %","")
  return float(value)

def send_email(receiver, value):
    sender = os.getenv('email_addr')
    password = os.getenv('PASSWORD')
    message = """
    This is to inform you that the percentage change of the stock is {}%
    """.format(value)
    message = MIMEText(message)
    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = 'Change notification'

    server = smtplib.SMTP('smtp.office365.com', 587)
    server.starttls()
    server.login(sender, password)
    server.sendmail(sender, receiver, message.as_string())
    server.quit()

def main():
  driver = get_driver()
  value = percentage_change(driver)
  if (value < 0.1):
    send_email('ngrfieqjxnphxlpkkw@bvhrk.com',value)

print(main())