from openpyxl import workbook, load_workbook
import datetime as dt

today_date = dt.datetime.today().strftime('%d/%m/%Y')

wb = load_workbook("Data.xlsx")
ws = wb.active

for row in ws.iter_rows(min_row=1, max_row=ws.max_row, min_col=1, max_col=1):
    for cell in row:
        if cell.value is None or cell.value == "":
            print(f"Cell {cell.coordinate} is empty.")
        else:
            print(f"Cell {cell.coordinate} has value: {cell.value}")
