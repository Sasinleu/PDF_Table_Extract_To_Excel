import pdfplumber as pdf
import pandas as pd

pd.set_option('display.max_rows', None)      # Show all rows
pd.set_option('display.max_columns', None)   # Show all columns
pd.set_option('display.width', None)         # Prevent line wrapping
pd.set_option('display.max_colwidth', None)  # Show full text inside cells
'''
PDF_Path = [
    "C:\\Users\\sasin\\PycharmProjects\\PDF_Table_Extract_To_Excel\\Pages from A350MPDREV11_01Jul25.pdf"
]

# path = ["C:\\Users\sasin\PycharmProjects\PDF_Table_Extract_To_Excel\Appendix_A.pdf"]
for A in PDF_Path:
    with pdf.open(A) as file:
        total_pages = len(file.pages)
        print("Length of PDF =", total_pages)

        length = 3  # limit to first 3 pages for testing

        all_tables = []  # to store DataFrames

        for i in range(0, length):
            page = file.pages[i]
            table = page.extract_table()

            if table:  # only process if a table is found
                df = pd.DataFrame(table[1:-1], columns=table[0])
                all_tables.append(df)
            else:
                print(f"No table found on page {i + 1}")

        # If multiple pages contain tables → combine them
    if all_tables:
        final_df = pd.concat(all_tables, ignore_index=True)
        print(final_df)
    else:
        print("No tables extracted.")


   text = page.extract_text()
   print(type(text))
   print(len(text))
   print('//////////////////////////////////////////////////////////////////////////')
   print(text)
'''
df = pd.read_csv('Pages from A350MPDREV11_01Jul25.csv')
#print(df)

# Show first 100 rows
print("===== FIRST 100 ROWS =====")
print(df.head(100))

# Show last 100 rows
print("\n===== LAST 100 ROWS =====")
print(df.tail(100))