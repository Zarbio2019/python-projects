# Author: Zarbio Romulo

import yagmail
import os

sender = 'app7flask@gmail.com'
receiver = 'app7flask@gmail.com'

subject = """
This is the subject!
"""

# convert "contents" from string to list, add file
contents = ["""
Here is the content of the email! 
Hi!
""", 'text.txt']

yag = yagmail.SMTP(user=sender, password=os.getenv('PASSWORD')) # Set your own PASSWORD in Repl Secrets
yag.send(to=receiver, subject=subject, contents=contents)
print("Email Sent!")