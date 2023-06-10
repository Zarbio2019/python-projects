# Author: Zarbio Romulo

from pathlib import Path
from datetime import datetime

# example 1
#path = Path('files/December/a.txt')
#stats = path.stat() # get info of file (size, time)
#second_created = stats.st_ctime

#print(stats)
#print(second_created)

root_dir = Path('files')

for path in root_dir.glob("**/*"):
  if path.is_file():
    created_date = datetime.fromtimestamp(path.stat().st_ctime) # to data and time, ex: 2021-11-02 18:36:43.059385
    
    created_date_str = created_date.strftime("%Y-%m-%d_%H:%M:%S") # to format AAAA-MM-DD hh:MM:ss
    new_filename = created_date_str + '_' + path.name
    new_filepath = path.with_name(new_filename)
    path.rename(new_filepath)