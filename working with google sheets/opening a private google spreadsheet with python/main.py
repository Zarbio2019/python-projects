# Author: Zarbio Romulo

# Feel free to copy the data of the spreadsheeet in the link to a new spreadsheet in your Google Sheets account:
# https://docs.google.com/spreadsheets/d/1D7U4A9c-hwWWYokmGWAQnUTKsyvEmV9syig8NJuVa84/edit?usp=sharing

import gspread

gc = gspread.service_account('secrets.json')

spreadsheet = gc.open('weather_private') # name of the spreadsheet

# Get a worksheet by index
# worksheet1 = spreadsheet.get_worksheet(0) # get the name of the sheet, don't the data

# Get a worksheet by name 
worksheet1 = spreadsheet.worksheet('2013')

data = worksheet1.get_all_records() # get the data of the sheet, in  list of dictionaries
print(data)
#print(data[10]) # get data in row 10
