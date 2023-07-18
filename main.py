from pdf2docx import Converter

pdf_file = r'E:\profiles\Jack_Lee_Resume.pdf'
docx_file = r'D:\study\test.docx'

# convert pdf to docx
cv = Converter(pdf_file)
cv.convert(docx_file)      # all pages by default
cv.close()