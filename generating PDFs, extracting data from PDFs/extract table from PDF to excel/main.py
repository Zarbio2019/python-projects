# Author: Zarbio Romulo

import tabula

table = tabula.read_pdf('Table and Text.pdf', pages=1) # pages = number of the page

#print(table)
print(type(table[0]))

table[0].to_excel('output.xlsx', index=None)