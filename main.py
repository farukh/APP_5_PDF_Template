import fpdf
import pandas as pd

df = pd.read_csv('topics.csv', sep=',')
# PDF file general settings
pdf = fpdf.FPDF(orientation='P', unit='mm', format='A4')
pdf.set_auto_page_break(auto=False, margin=0)
for index, row in df.iterrows():
    # SET HEADER
    pdf.add_page()  # Add Page to Pdf Document
    # Page Settings
    pdf.set_font(family='Times', style='B', size=24)
    pdf.set_text_color(100, 100, 100)
    # Page Contents
    pdf.cell(w=0, h=12, txt=row['Topic'], align='L', ln=1, border=0)
    for y in range(2,30): #Add Page Lines
       pdf.line(10,y*10,200,y*10)

    # SET FOOTER
    pdf.ln(265)
    pdf.set_font(family='Times', style='I', size=8)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=10, txt=row['Topic'], align='R')

    for i in range(row['Pages'] - 1):
        pdf.add_page()
        for y in range(2, 30): #Add Page Lines
            pdf.line(10, y * 10, 200, y * 10)
        # Follwoing loop is same as above, 20 to 298 with inc or 10
        for y in range (20, 298, 10):
            pdf.line(10, y, 200, y)

        # SET FOOTER
        pdf.ln(273)
        pdf.set_font(family='Times', style='I', size=8)
        pdf.set_text_color(100, 100, 100)
        pdf.cell(w=0, h=10, txt=row['Topic'], align='R')

# Generate PDF with file name
pdf.output("output.pdf")
