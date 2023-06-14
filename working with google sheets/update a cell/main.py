# Author: Zarbio Romulo

import gspread

# Establish connection
gc = gspread.service_account('secrets.json')

# Get spreadsheet
spreadsheet = gc.open('weather_private') 

# Get worksheet
worksheet1 = spreadsheet.worksheet('2013')

# Update a cell 
worksheet1.update('E5', -29)

# Update a cell based on row-column 
worksheet1.update_cell(5, 5, -39)  # row, col, value
