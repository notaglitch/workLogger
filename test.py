from openpyxl import workbook, load_workbook
import datetime as dt

today_date = dt.today().strftime('%d-%m-%Y')
wb = load_workbook("Data.xlsx")
ws = wb.active()

for rows in wn

wb.save("Data.xlsx")