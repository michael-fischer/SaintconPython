import xlrd

file = 'saintcon.xls'
book = xlrd.open_workbook(file)
sheet = book.sheet_by_name('Saintcon')

print('there are {} rows with {} columns'.format(sheet.nrows, sheet.ncols))

for r in range(sheet.nrows):
    for c in range(sheet.ncols):
        print("'{}'\t".format(sheet.cell(r, c).value, end = '')),
        print("'{}'\t".format(sheet.cell(r, c).ctype, end = '')),
    print("")


