import xlrd
wb = xlrd.open_workbook('RawData.xlsx')
sh1=wb.sheet_by_name(u'CSTRLowLYS conc.')
sh2=wb.sheet_by_name(u'CSTRLowMEA conc.')
x=sh1.col_values(1,start_rowx=1) #Time
y=sh1.col_values(7,start_rowx=1) #lysine co2 loading
x1=sh2.col_values(1,start_rowx=1)
y1=sh2.col_values(6,start_rowx=1)#MEa co2 loading
import matplotlib.pyplot as plt
plt.plot(x,y, label='K$^{+}$LYS$^{-}$')
plt.plot(x1,y1, label='MEA')
plt.legend(loc='best')
plt.xlabel('Reaction Time (min)')
plt.ylabel('CO$_{2}$ loading (mol CO$_{2}$/mol lysine/MEA)')
plt.savefig('lowcstrcompar.png')
plt.show()