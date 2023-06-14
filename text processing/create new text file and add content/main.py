# Author: Zarbio Romulo

content = """First text


Second text"""

#file = open('file1.txt', 'w') # w = overwrite
#file.write('First text\n')
#file.write('Second text')
#file.close()

with open('file1.txt', 'w') as file:
  file.write(content)
