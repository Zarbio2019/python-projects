# Author: Zarbio Romulo

import pandas

# url from sheet = https://docs.google.com/spreadsheets/d/1D7U4A9c-hwWWYokmGWAQnUTKsyvEmV9syig8NJuVa84/edit?usp=sharing"
# with pandas you can onlyread sheet
# to read a sheet change url to gviz/tq?tqx=out:csv&sheet=2013
# where sheet is the specific sheet
url_sheet1 = "https://docs.google.com/spreadsheets/d/1D7U4A9c-hwWWYokmGWAQnUTKsyvEmV9syig8NJuVa84/gviz/tq?tqx=out:csv&sheet=2013"
url_sheet2 = "https://docs.google.com/spreadsheets/d/1D7U4A9c-hwWWYokmGWAQnUTKsyvEmV9syig8NJuVa84/gviz/tq?tqx=out:csv&sheet=2014"
data1 = pandas.read_csv(url_sheet1)
data2 = pandas.read_csv(url_sheet2)

print(data1)
print(data2)