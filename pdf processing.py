import PyPDF2
import sys
list_pdf=sys.argv[1:]
def pdfmerger (listPdf) :
merger=PyPDF2.PdfFileMerger()
for i in listPdf :
print(i)
merger.append(i)
merger.write('super.pdf')
pdfmerger(list_pdf)