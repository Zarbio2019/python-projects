# Author: Zarbio Romulo

from pathlib import Path

root_dir = Path('files')

for i in range(10, 21): # from 10 to 20
  filename = str(i) + '.txt'
  filepath = root_dir / Path(filename)
  filepath.touch() # create empty files from 11.txt to 20.txt
  