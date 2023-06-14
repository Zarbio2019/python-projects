# Author: Zarbio Romulo
import sqlite3
from fpdf import FPDF

con = sqlite3.connect('database.db')
cur = con.cursor()

cur.execute('PRAGMA table_info(ips)') # info from table "ips"
columns = cur.fetchall()
print(columns) # list of tuples

pdf = FPDF(orientation='P', unit='pt', format='A4') # P = portrait, pt = point
pdf.add_page()

# for columns
for column in columns:
  pdf.set_font(family='Times', style='B', size=14) # for columns, B = Bold
  pdf.cell(w=100, h=30, txt=column[1], border=1)

pdf.ln() # break line

# for rows
cur.execute("SELECT * FROM 'ips'")
rows = cur.fetchall()

for row in rows:
  for element in row: # iterate over the values of the row
    pdf.set_font(family='Times', size=14)
    pdf.cell(w=100, h=30, txt=str(element), border=1)
  pdf.ln() # break line

pdf.output('output.pdf')