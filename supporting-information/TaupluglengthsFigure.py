import xlrd
import matplotlib.pyplot as plt
wb = xlrd.open_workbook('RawData.xlsx')
sh1 = wb.sheet_by_name(u'TAU')
x1 = sh1.col_values(6,start_rowx=1,end_rowx=36)  # distance
y1 = sh1.col_values(4,start_rowx=1,end_rowx=36)  # plug length
x2 = sh1.col_values(15,end_rowx=11)  # distanceforfit

# pluglengthforfit; Fit being y= 2122.212*exp((-6.127482*(10^-5))*x) with units of microns for distance and plug length
y2 = sh1.col_values(16,end_rowx=11)

plt.plot(x1, y1, 'ro', x2, y2)
plt.xlabel('Distance (microns)')
plt.ylabel('Plug Length (microns)')
plt.savefig('TAUpluglengths.png')
plt.show()
