import smtplib # library standard for email
import os

sender = 'automateeverythingwithpython@hotmail.com'
receiver = 'app7flask@gmail.com'
password = 'python12345678' # sender's password, registered in local computer and save as a plain python string
#password = os.getenv('PASSWORD') # password registered in Replit

message = """\
Subject: Hello Hello

This is Ardit!
Just wanted to say hi!
"""

# for outlook:
# domain = smtp.office365.com
# port = 587
server = smtplib.SMTP('smtp.office365.com', 587)
server.starttls() # TLS protocol to send emails in an encrypted form
server.login(sender, password)
server.sendmail(sender, receiver, message)
server.quit()
