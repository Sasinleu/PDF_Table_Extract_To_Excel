import pdfplumber as pdf
#path = ["C:\\Users\sasin\PycharmProjects\PDF_Table_Extract_To_Excel\Appendix_A.pdf"]
#for i in path:
with pdf.open("C:\\Users\sasin\PycharmProjects\PDF_Table_Extract_To_Excel\Appendix_A.pdf") as file:
   first_page = file.pages[1].page_number
   print(first_page)

