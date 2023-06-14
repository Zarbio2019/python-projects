# Author: Zarbio Romulo

import json

file = open('data.json')
data = json.load(file)
#print(data)
#print(type(data)) # dict
print(data['island']) # there are 2 definitions for this word

def define(word):
  word = word.lower()
  if word in data:
    return data[word]
  # by default return None

# console
word = input('Please enter a word: ')
definition = define(word)
#print(definition)

if definition:
  for item in definition: # to print without brackets of list
    print(item)
else:
  print("Word was not found!")