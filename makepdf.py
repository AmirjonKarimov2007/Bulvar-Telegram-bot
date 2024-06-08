from fpdf import FPDF

# PDF yaratish obyekti
pdf = FPDF()
pdf.add_page()

# Matn qo'shish
pdf.set_font("Arial", size = 12)
pdf.cell(200, 10, txt = "Hello, world!", ln = True, align = 'C')

# PDFni saqlash
pdf.output("hello_world.pdf")