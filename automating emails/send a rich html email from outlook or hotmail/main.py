# Author: Zarbio Romulo

import smtplib
from email.mime.text import MIMEText # message in HTML
from email.mime.multipart import MIMEMultipart # message in HTML

sender = 'automateeverythingwithpython@hotmail.com'
receiver = 'app7flask@gmail.com'
password = 'python12345678'

# MIME = Multi-purpose Internet Mail Extensions
message = MIMEMultipart()
message['From'] = sender
message['To'] = receiver
message['Subject'] = 'Hello again!'

body = """
<h2>Hi there!</h2>
There are only two cats flying today!
Let's hope for more!
"""
mimetext = MIMEText(body, 'html') # 'html' = HTML format, 'plain' = text format
message.attach(mimetext)

server = smtplib.SMTP('smtp.office365.com', 587)
server.starttls()
server.login(sender, password)
message_text = message.as_string() # dictionary to string
print(message_text)
server.sendmail(sender, receiver, message_text)
server.quit()
