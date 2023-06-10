# Author: Zarbio Romulo

from pathlib import Path

root_dir = Path('.')
search_term = '14' # search name that contains "14"

for path in root_dir.rglob("*"):
  if path.is_file(): # for files
    if search_term in path.stem:
      print(path.absolute()) # absolute or full path of a file