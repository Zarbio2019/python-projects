# Author: Zarbio Romulo

from pathlib import Path 
import zipfile

root_dir = Path('files')
archive_path = root_dir / Path('archive.zip')

with zipfile.ZipFile(archive_path, 'w') as zf:
  for path in root_dir.rglob("*.txt"):
    zf.write(path) # create .zip file
    path.unlink() # delete the .txt files
