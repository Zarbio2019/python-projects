# Author: Zarbio Romulo

from pathlib import Path

root_dir = Path('destination')

for path in root_dir.glob("*.csv"):
  with open(path, 'wb') as file: # wb = write binary mode
    file.write(b'')# delete content of a file
  path.unlink() # delete file