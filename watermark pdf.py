import PyPDF2
with open('super.pdf','rb') as surfile :
with open('wtr.pdf','rb') as wtrfile :
readers=PyPDF2.PdfFileReader(surfile)
readerw=PyPDF2.PdfFileReader(wtrfile)
n=readers.numPages
pagew=readerw.getPage(0)
with open('wtrsuper.pdf','wb') as file :
writer=PyPDF2.PdfFileWriter()
for i in range(n) :
pages=readers.getPage(i)
pages.mergePage(pagew)
writer.addPage(pages)
writer.write(file)
