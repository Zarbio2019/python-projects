# Author: Zarbio Romulo

import yagmail
import os
import time
from datetime import datetime as dt

sender = 'app7flask@gmail.com'
receiver = 'fbcmakfsd@emltmp.com'

subject = """
This is the subject!
"""
contents = """
Here is the content of the email! 
Hi!
"""

while True:
  now = dt.now()
  if now.hour == 13 and now.minute == 18: # 13:18 pm
    yag = yagmail.SMTP(user=sender, password=os.getenv('PASSWORD'))
    yag.send(to=receiver, subject=subject, contents=contents)
    print("Email Sent!")
    time.sleep(60)