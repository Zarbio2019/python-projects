# Author: Zarbio Romulo

from pathlib import Path

root_dir = Path('files')

for path in root_dir.glob("**/*"):
  if path.is_file():
    path_parts = path.parts
    #print(path_parts) # ex: ('files', '2021', 'November', 'd.txt')
    subfolders = path.parts[1:-1]
    #print(subfolders) # ex: ('2021', 'November')

    new_filename = "-".join(subfolders) + '-' + path.name
    print(new_filename)
    new_filepath = path.with_name(new_filename)
    path.rename(new_filepath)