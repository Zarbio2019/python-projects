# Author: Zarbio Romulo

from fpdf import FPDF # package for PDF

pdf = FPDF(orientation='P', unit='pt', format='A4') # p = portrait, pt = point

#help(pdf)
#dir(pdf) # show methods

pdf.add_page()

# build content
pdf.image('tiger.jpeg', w=80, h=50)
#pdf.image('tiger.jpeg', w=80, h=50, x=50)

# each cell must to have .set_font and .cell
pdf.set_font(family='Times', style='B', size=24)
pdf.cell(w=0, h=50, txt="Malayan Tiger", align='C', ln=1) # C = center, ln=1 = 1 break line

pdf.set_font(family='Times', style='B', size=14)
pdf.cell(w=0, h=15, txt='Description', ln=1)
#pdf.cell(w=0, h=15, txt='Description', ln=1, border=1) # show border

pdf.set_font(family='Times', size=12)
txt1 = """The Malayan tiger is a tiger from a specific population of the Panthera tigris tigris subspecies that is native to Peninsular Malaysia.[5] This population inhabits the southern and central parts of the Malay Peninsula and has been classified as critically endangered on the IUCN Red List since 2015. As of April 2014, the population was estimated at 80 to 120 mature individuals with a continuous declining trend"""
pdf.multi_cell(w=0, h=15, txt=txt1) # multi_cell = adjust multi line

pdf.set_font(family='Times', style='B', size=14)
pdf.cell(w=100, h=25, txt='Kingdom:')

pdf.set_font(family='Times', size=14)
pdf.cell(w=100, h=25, txt='Animalia', ln=1)

pdf.set_font(family='Times', style='B', size=14)
pdf.cell(w=100, h=25, txt='Phylum:')

pdf.set_font(family='Times', size=14)
pdf.cell(w=100, h=25, txt='Chordata', ln=1)

pdf.output('output.pdf')
