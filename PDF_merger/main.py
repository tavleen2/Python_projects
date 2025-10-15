from PyPDF2 import PdfWriter

merger = PdfWriter()

pdfs = []
num = int(input("How many Pdfs do you want to merge ? : "))

for i in range(0, num):
    name = input(f"Enter the name of pdf {i+1} : ")
    pdfs.append(name)

for pdf in pdfs:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()