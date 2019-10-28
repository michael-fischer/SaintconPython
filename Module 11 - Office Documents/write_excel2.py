import xlwt
import datetime

headers = ['Date', 'Quantity']
date = datetime.datetime(2018, 12, 25)

new_book = xlwt.Workbook()
new_sheet = new_book.add_sheet('Saintcon')

date_format = xlwt.XFStyle()
date_format.num_format_str = 'yyyy-MM-dd'

row = 0
col = 0
line = new_sheet.row(row)
for header in headers:
    line.write(col, header)
    col +=1

for day in range(12):
    row += 1
    line = new_sheet.row(row)
    line.write(0, date, date_format)
    if row == 1:
        line.write(1, row)
    else: 
        formula = 'B{} + {}'.format(row, row)
        line.write(1, xlwt.Formula(formula))
    date = date + datetime.timedelta(days=1)

new_book.save('saintcon.xls')
