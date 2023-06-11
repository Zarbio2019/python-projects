# Author: Zarbio Romulo

import pandas
from fpdf import FPDF

df = pandas.read_excel('data.xlsx')
# print(df)

for index, row in df.iterrows():
  #print(row)
  pdf = FPDF(orientation='P', unit='pt', format='A4')
  pdf.add_page()

  pdf.set_font(family='Times', style='B', size=24)
  pdf.cell(w=0, h=50, txt=row['name'], align='C', ln=1) # title

  for column in df.columns[1:]:
    pdf.set_font(family='Times', style='B', size=14)
    pdf.cell(w=100, h=25, txt=f"{column.title()}:")
    #pdf.cell(w=100, h=25, txt="Kingdom")

    pdf.set_font(family='Times', size=14)
    pdf.cell(w=100, h=25, txt=row[column], ln=1)

  pdf.output(f"{row['name']}.pdf") # file name