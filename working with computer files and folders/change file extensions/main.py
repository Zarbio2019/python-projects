# Author: Zarbio Romulo

from pathlib import Path

root_dir = Path('files')

for path in root_dir.rglob("*.csv"): # rglob("*.csv") = glob("**/*.csv")
  if path.is_file():
    new_filepath = path.with_suffix(".txt")
    path.rename(new_filepath)
    