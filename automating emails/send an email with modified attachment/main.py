# Author: Zarbio Romulo

import yagmail
import os
import pandas

sender = 'app7flask@gmail.com'

yag = yagmail.SMTP(user=sender, password=os.getenv('PASSWORD')) # Set your own PASSWORD in Repl Secrets

df = pandas.read_csv('contacts.csv')

# write content in a file
def generate_file(filename, content):
  with open(filename, 'w') as file:
    file.write(str(content))

# iteration
for index, row in df.iterrows():
  name = row['name']
  filename = name + ".txt"
  amount = row['amount'] # int
  receiver_email = row['email']
  
  generate_file(filename, amount)
  
  subject = "This is the subject!"
  contents = [f"""
  Hey, {name} you have to pay {amount}
  Bill is attached!""",
  filename,
  ]
  
  yag.send(to=receiver_email, subject=subject, contents=contents)
  print("Email Sent!")