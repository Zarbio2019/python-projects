# Author: Zarbio Romulo

from pathlib import Path

root_dir = Path('files') # folder files
file_paths = root_dir.iterdir() # list files
#print(list(file_paths))

print(Path.cwd()) # current working directory

for path in file_paths:
  new_filename = "new-" + path.stem + path.suffix
  new_filepath = path.with_name(new_filename) #files/new-abc.txt
  #new_file = Path(new_filename) # empty
  print(new_filepath)
  path.rename(new_filepath) # rename file name
  