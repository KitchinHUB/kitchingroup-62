import xlrd
wb = xlrd.open_workbook('RawData.xlsx')
sh2=wb.sheet_by_name(u'MEA')
sh3=wb.sheet_by_name(u'GLY')
sh4=wb.sheet_by_name(u'TAU')
sh5=wb.sheet_by_name(u'PRO')
sh6=wb.sheet_by_name(u'LYS')
tm=sh2.col_values(9,start_rowx=1,end_rowx=44)
cm=sh2.col_values(11,start_rowx=1,end_rowx=44)#MEA data
tg=sh3.col_values(9,start_rowx=1,end_rowx=37)
cg=sh3.col_values(11,start_rowx=1,end_rowx=37)#GLY data
tt=sh4.col_values(9,start_rowx=1,end_rowx=36)
ct=sh4.col_values(11,start_rowx=1,end_rowx=36)#TAU data
tp=sh5.col_values(9,start_rowx=1,end_rowx=33)
cp=sh5.col_values(11,start_rowx=1,end_rowx=33)#PRO data
tl=sh6.col_values(9,start_rowx=1,end_rowx=59)
cl=sh6.col_values(11,start_rowx=1,end_rowx=59)#LYS data
import matplotlib.pyplot as plt
plt.plot(tl,cl,color='#FF8000',marker='D', label='LYS')
plt.plot(tm,cm,color='r',marker='o', label='MEA')
plt.plot(tg,cg,color='g',marker='v', label='GLY')
plt.plot(tt,ct,color='m',marker='^', label='TAU')
plt.plot(tp,cp,color='b',marker='s', label='PRO')
plt.legend(loc='bottom right')
plt.xlabel('Time (s)')
plt.ylabel('Concentration of absorbed CO$_{2}$ (M)')
plt.savefig('summaryplot.png')
plt.show()