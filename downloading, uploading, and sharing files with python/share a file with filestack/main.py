# Author: Zarbio Romulo

from filestack import Client

api_key = "AViVqp7suSQWWEdrl6hf9z"

client = Client(api_key)
new_link = client.upload(filepath='file.txt')

print(new_link.url)