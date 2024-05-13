from fpdf import FPDF
import pandas as pd

df = pd.read_csv('topics.csv', sep=',')
# PDF file general settings
pdf = FPDF(orientation='P', unit='mm', format= 'A4')

for index, row in df.iterrows():
     #for page in df['Pages']:
     # Add Page to Pdf Document
     pdf.add_page()
     # Page Settings
     pdf.set_font(family='Times', style='B', size=24 )
     pdf.set_text_color(100,100,100)
     # Page Contents
     pdf.cell(w=0, h=12, txt=row['Topic'], align='L', ln=1, border=0)
     # pdf.line(0,12)
     pdf.line(10,21,200,21)
     # e.g. if value of pages is 3 then  row['Pages'] = [0,1,2] then
     for i in range(row['Pages']-1):
        # for page in df['Pages']:
        # Add Page to Pdf Document
        pdf.add_page()

# Generate PDF with file name
pdf.output("output.pdf")