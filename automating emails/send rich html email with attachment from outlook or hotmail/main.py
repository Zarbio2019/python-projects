# Author: Zarbio Romulo

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

sender = 'automateeverythingwithpython@hotmail.com'
receiver = 'app7flask@gmail.com'
password = 'python12345678'

message = MIMEMultipart()
message['From'] = sender
message['To'] = receiver
message['Subject'] = 'Hello again!'

body = """
<h2>Hi there!</h2>
There are only two cats flying today!
Let's hope for more!
"""
mimetext = MIMEText(body, 'html')
message.attach(mimetext)

# attachment file
attachment_path = 'tiger.jpeg'
attachment_file = open(attachment_path, 'rb') # 'rb' = read binary mode
payload = MIMEBase('application', 'octate-stream')
payload.set_payload(attachment_file.read())
encoders.encode_base64(payload)
payload.add_header('Content-Disposition', 'attachment', filename=attachment_path)
message.attach(payload)

# send file
server = smtplib.SMTP('smtp.office365.com', 587)
server.starttls()
server.login(sender, password)
message_text = message.as_string()
print(message_text)
server.sendmail(sender, receiver, message_text)
server.quit()
