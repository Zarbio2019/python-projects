# filter only those file names from 1st of November on to the 20th of November

# read file
from pathlib import Path 

root_dir = Path('files')
filenames = root_dir.iterdir()
filenames_str = [filename.name for filename in filenames]
filenames_str

# return:
#['Nov-12.txt',
# 'billy_Nov-13.txt',
# 'november-14.txt',
# 'nov-20.txt',
# 'Nov-22.txt',
# 'November-24.txt',
# 'Oct-17.txt']

# process
import re

pattern = re.compile("nov[a-z]*-(?:[1-9]|1[0-9]|20).txt", re.IGNORECASE)
matches = [filename for filename in filenames_str if pattern.findall(filename)]
matches

#['Nov-12.txt', 'billy_Nov-13.txt', 'november-14.txt', 'nov-20.txt']
