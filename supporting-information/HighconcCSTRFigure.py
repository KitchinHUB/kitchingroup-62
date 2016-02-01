import xlrd
wb = xlrd.open_workbook('RawData.xlsx')
sh1 = wb.sheet_by_name(u'CSTR-HighLYS conc.')
sh2 = wb.sheet_by_name(u'CSTR-HighMEA conc.')

x = sh1.col_values(10,start_rowx=1)  # Time
y = sh1.col_values(7,start_rowx=1)  #lysine co2 loading
x1 = sh2.col_values(1,start_rowx=1)
y1 = sh2.col_values(7,start_rowx=1)  # MEa co2 loading

import matplotlib.pyplot as plt
plt.plot(x, y, label='K$^{+}$LYS$^{-}$')
plt.plot(x1, y1, label='MEA')
plt.legend(loc='best')
plt.xlabel('t*(Q/V) (unitless)')
plt.ylabel('CO$_{2}$ loading (mmol CO$_{2}$/g solution')
plt.savefig('highcstrcompar.png')
plt.show()
