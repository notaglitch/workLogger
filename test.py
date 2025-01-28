from openpyxl import workbook, load_workbook
import datetime as dt

# Define the sheet name
sheet_name = "main"
# Today's date
today_date = dt.today().strftime('%d-%m-%Y')

open_file = pd.read_excel("Data.xlsx", sheet_name=sheet_name)

last_row_date = open_file.iloc[-1, 0].strftime('%d-%m-%Y')

def write_to_file(last_row_date, today_date):
    if last_row_date == today_date:
        print("Up to date")
    else:
        print("Not up to date")

write_to_file(last_row_date, today_date)

wb.save("Data.xlsx")