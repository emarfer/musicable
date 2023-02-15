import gspread

sa = gspread.service_account()
sh = sa.open('prueba')

wks = sh.worksheet('Hoja 1')

print(f'Rows: {wks.row_count}')

sheetid = '1nq2hVRnPx46BXrB4y_XAqRMO_8qpW-5PwQjRZbQzwAY'
sh = sa.open_by_key(sheetid)
worksheet_list = sh.worksheets()
print(worksheet_list)
