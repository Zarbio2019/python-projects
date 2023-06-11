# Author: Zarbio Romulo

import tabula

table = tabula.read_pdf('weather.pdf', pages=1) # pages = number of the page

#print(table)
print(type(table[0]))

table[0].to_csv('output.csv', index=None)