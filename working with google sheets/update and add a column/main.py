import gspread

# Establish connection
gc = gspread.service_account('secrets.json')

# Get spreadsheet
spreadsheet = gc.open('weather_private') 

# Get worksheet
worksheet1 = spreadsheet.worksheet('2013')

existing_column = worksheet1.get_values('E2:E25')

# celsius to fahrenheit
new_column = [[round((float(i[0]) * 9/5 + 32), 1)] for i in existing_column] # 1 = 1 decimal
# [[ = to convert to list of list
#new_column = [i[0] for i in existing_column]
print(new_column)

worksheet1.update('G1:G25', [['Fahrenheit']] + new_column) # header Fahrenheit
