from openpyxl import workbook, load_workbook
import datetime as dt

today_date = dt.datetime.today().strftime('%d/%m/%Y')
wb = load_workbook("Data.xlsx")
ws = wb.active

date_col = ws['A1'].value
focus_session_col = ws['B1'].value
last_row = ws.max_row

ws[f"A{last_row}"] = today_date

wb.save("Data.xlsx")