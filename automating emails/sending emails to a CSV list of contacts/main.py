# Author: Zarbio Romulo

import yagmail
import os
import pandas

sender = 'your_gmail_address@gmail.com'

subject = """
This is the subject!
"""

# The password should be a Gmail app password. 
# Your Gmail account password won't work.
yag = yagmail.SMTP(user=sender, password="PASSWORD") # PASSWORD = Your Gmail App Password

df = pandas.read_csv('contacts.csv') # use panda data frame for CSV file

for index, row in df.iterrows():
  #print(index)
  #print(row['email']) # get emails
  contents = f"""
Hi {row['name']} the content of the email! 
Hi!
"""
  yag.send(to=row['email'], subject=subject, contents=contents)
  print("Email Sent!")