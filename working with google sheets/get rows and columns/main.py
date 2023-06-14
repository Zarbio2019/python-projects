# Author: Zarbio Romulo
# Get a copy of the data here: https://docs.google.com/spreadsheets/d/1OS3sMy3jUDED4f-7J4n8vr8CBLK3jyKlLWJxTTmu-sI/edit?usp=sharing

import gspread

# Establish connection
gc = gspread.service_account('secrets.json')

# Get spreadsheet
spreadsheet = gc.open('weather_private') 

# Get worksheet
worksheet1 = spreadsheet.worksheet('2013')

data = worksheet1.get_all_records()

print(data[0]) # get data from row 1

# Get a row or rows by cells
rows = worksheet1.get_values('A5:F7') # range of rows

# Get a row by index 
rows = worksheet1.row_values(3)

# Get a col or cols by cells
rows = worksheet1.get_values('C5:C25') # range of cols

print(rows)

# Get a column by index
column = worksheet1.col_values(2) # get col 2 (1 = col 1, 2 = col 2)
column = worksheet1.col_values(2)[1:] # [1:] = without the column name

print(column)
