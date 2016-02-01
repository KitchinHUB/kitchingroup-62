import xlrd
wb = xlrd.open_workbook('selexol methods graph data.xlsx')
sh1 = wb.sheet_by_name(u'Sheet1')
sh2 = wb.sheet_by_name(u'Sheet2')
x = sh1.col_values(0,start_rowx=1)  # wavenumber
y = sh1.col_values(1,start_rowx=1)  #neat spectrum
x1 = sh2.col_values(0,start_rowx=1)
y1 = sh2.col_values(1,start_rowx=1)  # in equilibria with 40 bar co2

import matplotlib.pyplot as plt
plt.plot(x, y, label='Neat Solvent')
plt.plot(x1, y1, label='In equilibrium with 40 bar CO$_{2}$')
plt.legend(loc='upper left',fontsize=13)
plt.xlabel('Wavenumber (cm$^{-1}$)')
plt.ylabel('Raman intensity (a.u.)')
plt.savefig('fig7.png')
plt.show()
