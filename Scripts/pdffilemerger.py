import PyPDF2
import sys

inputs=sys.argv[1:]

def pdf_combiner(pdf_list):
    merger=PyPDF2.PdfFileMerger(inputs)
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write('super.pdf')


# with open('011 dummy.pdf','rb') as file:
#     reader=PyPDF2.PdfFileReader(file)
#     page=reader.getPage(0)
#     page.rotateClockwise(180)
#     writer=PyPDF2.PdfFileWriter()
#     writer.addPage(page)
#     with open('tilt.pdf','wb') as newfile:
#         writer.write(newfile)