# Author: Zarbio Romulo
# Get a copy of the data here: https://docs.google.com/spreadsheets/d/1OS3sMy3jUDED4f-7J4n8vr8CBLK3jyKlLWJxTTmu-sI/edit?usp=sharing

import gspread
import re

# Establish connection
gc = gspread.service_account('secrets.json')

# Get spreadsheet
spreadsheet = gc.open('weather_private') 

# Get worksheet
worksheet1 = spreadsheet.worksheet('2013')

# Get cell
cell1 = worksheet1.get_values('D5')[0][0] # [0][0] = index of list

# Get cell using acell
cell2 = worksheet1.acell('D5').value

# Search for a cell 
cell3 = worksheet1.find('-10')

# Search for many cells 
cells = worksheet1.findall('-9')

# Search for partial matches
# for example to search value 99
reg = re.compile(r'99') # regular expression
cells = worksheet1.findall(reg)

for cell in cells:
  print(cell.row, cell.col) # get coordinates of cell
