from openpyxl import workbook, load_workbook
import datetime as dt

today_date = dt.datetime.today().strftime('%d/%m/%Y')

wb = load_workbook("Data.xlsx")
ws = wb.active
print(today_date)

date_col = 'A1'
focus_session_col = 'B1'



wb.save("Data.xlsx")