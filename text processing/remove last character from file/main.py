# Author: Zarbio Romulo

with open('file3.csv', 'r') as file:
  content = file.read()

print(content[:-1]) # .1 = remove the last caracter
#print(content[0:-1])

modified_content = content[:-1]

# create in new file
with open('file3.csv', 'w') as file:
  file.write(modified_content)