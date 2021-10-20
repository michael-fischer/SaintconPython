import xlwt

headers = ['Date', 'Quantity']
data = {
    '12/25/2018': 1,
    '12/26/2018': 3,
    '12/27/2018': 6,
    '12/28/2018': 10,
    '12/29/2018': 15,
    '12/30/2018': 21,
    '12/31/2018': 28,
    '1/1/2019': 36,
    '1/2/2019': 45,
    '1/3/2019': 55,
    '1/4/2019': 66,
    '1/5/2019': 78,
}

new_book = xlwt.Workbook()
new_sheet = new_book.add_sheet('Saintcon')

row = 0
col = 0
line = new_sheet.row(row)
for header in headers:
    line.write(col, header)
    col +=1

row += 1
for d in data:
    line = new_sheet.row(row)
    line.write(0, d)
    line.write(1, data[d])
    row += 1

new_book.save('saintcon.xls')
