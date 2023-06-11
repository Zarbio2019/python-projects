# Author: Zarbio Romulo

import fitz # PyMuPDF library

with fitz.open("students.pdf") as pdf:

  # print only first page
  #page1 = pdf[0].get_text()
  #print(page1)
    
  text = ''
  for page in pdf:
    
    # separate with 20 times '-' each page
    #print(20*'-')
    #print(page.get_text())
    
    # extract all text in one variable
    text = text + page.get_text()
    print(text)
