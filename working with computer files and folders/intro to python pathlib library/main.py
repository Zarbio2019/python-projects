# Author: Zarbio Romulo

from pathlib import Path

p1 = Path('files/ghi.txt')
print(type(p1))

# dir(Path)

if not p1.exists(): # if not exist path

  # read file
  #with open(p1, 'r') as file:
  #  print(file.read())
  
  # write file  
  with open(p1, 'w') as file:
    file.write('Content 3')

print(p1.name) # get filename
print(p1.stem) # get filename without extension
print(p1.suffix) # get extension

p2 = Path('files') # folder files
print(list(p2.iterdir())) # iteration of files, list generator
# or
#for item in p2.iterdir():
#  print(type(item))
