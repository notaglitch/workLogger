import pandas as pd
from datetime import datetime as dt

# Change sheet name to your sheet name
sheet_name = "main"

# Today's date, change format to your desired format
today_date = datetime.today().strftime('%d-%m-%Y')

open_file = pd.read_excel("Data.xlsx", sheet_name=sheet_name)
try:
    first_empty_row = open_file[open_file.iloc[:,0].isna()].index[0]
    last_filled_row = first_empty_row - 1
    last_row_date = open_file.iloc[last_filled_row, 0].strftime('%d-%m-%Y')
    print(last_row_date)
except IndexError:
    last_filled_row = len(open_file) - 1
    last_row_date = open_file.iloc[last_filled_row, 0].strftime('%d-%m-%Y')
    if last_row_date == today_date:
        print("Today's date is already in the file")
    else:
        print(today_date)