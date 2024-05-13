from fpdf import FPDF
# PDF file general settings
pdf = FPDF(orientation='P', unit='mm', format= 'A4')
# Add Page to Pdf Document
pdf.add_page()
# Page Settings
pdf.set_font(family='Times', style='B', size=12 )
# Page Contents
pdf.cell(w=0, h=12, txt="Page Title", align='L', ln=1, border=1)

# Generate PDF with file name
pdf.output("output.pdf")