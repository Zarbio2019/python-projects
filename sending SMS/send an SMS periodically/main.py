# Author: Zarbio Romulo

# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
import time


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

while True:
  message = client.messages \
                  .create(
                      body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                      from_='+1000000000',
                      to='+2000000000'
                  )

  print(message.sid)
  time.sleep(60) # every 60 seconds
