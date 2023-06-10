# Author: Zarbio Romulo

from pathlib import Path

root_dir = Path('files') # folder file

# method 1: get filename of the subdirectory
#file_paths = root_dir.iterdir()
#
#for path in file_paths:
#  for filepath in path.iterdir():
#    print(filepath)

# method 2: get filename of the subdirectory
file_paths = root_dir.glob("**/*") # inside subfolders

for path in file_paths:
  #print(path) # files/November, files/December

  if path.is_file():
    parent_folder = path.parts[-2] # -2 = index of folder name
    new_filename = parent_folder + '-' + path.name
    print(new_filename)
    new_filepath = path.with_name(new_filename)
    path.rename(new_filepath) # ex: Nomvember-abc.txt