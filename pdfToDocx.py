from pdf2docx import parse
 
pdf_file = r"C:\Users\DELL\Desktop\INTERNSHIP\DSA GEEEKSFORGEEKS.pdf"
docx_file = r"C:\Users\DELL\Desktop\INTERNSHIP\DSA GEEEKSFORGEEKS.docx"
 
# convert pdf to docx
parse(pdf_file, docx_file)