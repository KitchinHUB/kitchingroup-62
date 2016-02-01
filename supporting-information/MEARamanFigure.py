import xlrd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

wb = xlrd.open_workbook('RawData.xlsx')
sh1=wb.sheet_by_name(u'MEARaman')
xf=sh1.col_values(0)  
yf=sh1.col_values(2)# Raman intensity postMF fingerprint region
xpf=sh1.col_values(3)
ypf=sh1.col_values(4)# Raman intensity preMF fingerprint region
xh=sh1.col_values(6,end_rowx=2583)
yh=sh1.col_values(7,end_rowx=2583)  # Raman intensity postMF high region
xph=sh1.col_values(9,end_rowx=2583)
yph=sh1.col_values(10,end_rowx=2583)# Raman intensity preMF high region

# data has been read in
fig = plt.figure()

# figure created
ax = fig.add_subplot(1,2,1)

# left subplot added
ax.plot(xpf,ypf, label='Pre-MF expt')  # plotting pre data

xpf = np.array(xpf)
ypf = np.array(ypf)
ymax = ax.get_ylim()[1] + ax.get_ylim()[0]
shadeu = (xpf > 1400) & (xpf < 1600)
ax.set_ylim(20, 100)
ax.fill_between(xpf[shadeu], y1=np.zeros(len(xpf[shadeu])),y2=ymax*np.ones(len(xpf[shadeu])),
                color='#C8C8C8')
shadei= (xpf>800) & (xpf<1000)

ax.fill_between(xpf[shadei],y1=np.zeros(len(xpf[shadei])),y2=ymax*np.ones(len(xpf[shadei])),color='#B8B8B8')
ax.plot(xf,yf, label='Post-MF expt')#plotting post data
ax.set_xlim([800,1800])
ax.legend(loc='upper right')
ax.set_xlabel('Wavenumber (cm$^{-1}$)')
ax.set_ylabel('Raman Intensity (a.u.)')
ax.set_yticklabels([])
ax.text(1450,30,r'CO$_{2}$$^{-}$')
ax.text(1420,27,r'Stretch')
ax.text(1130,76,r'1162')
ax.text(1145,79,r'$\bigtriangleup$',color='r')
ax.text(1030,92,r'1067')
ax.text(1045,95,r'$\bigcirc$',color='r')
ax.text(910,90,r'1017')
ax.text(950,92.5,r'$\bigstar$',color='r')
ax.text(850,35,r'CH$_{2}$')
ax.text(835,32,r'Twist')
ax.text(840,29,r'CCO')
ax.text(818,26,r'Stretch')
ax.text(1020,33,r'$\bigtriangleup$',color='r')
ax.text(1080,33,r'Carbamate',color='r')
ax.text(1020,30,r'$\bigstar$',color='r')
ax.text(1080,30,r'HCO$_{3}$$^{-}$',color='r')
ax.text(1020,26,r'$\bigcirc$',color='r')
ax.text(1080,26,r'CO$_{3}$$^{-2}$',color='r')
# plot with shading
ax = fig.add_subplot(1,2,2)

# right subplot added
ax.plot(xph,yph, label='Pre-MF expt')
xph = np.array(xph)
yph = np.array(yph)
ymax = ax.get_ylim()[1]
shadex = (xph > 3200) & (xph < 3400)
ax.fill_between(xph[shadex], y1=np.zeros(len(xph[shadex])),y2=ymax*np.ones(len(xph[shadex])),
                color='#D0D0D0')
shadeq = (xph>2800) & (xph< 3000)
ax.fill_between(xph[shadeq],y1=np.zeros(len(xph[shadeq])),y2=ymax*np.ones(len(xph[shadeq])), color='#A8A8A8')                
ax.plot(xh,yh, label='Post-MF expt')
ax.set_xlim([2800,3800])

ax.set_xlabel('Wavenumber (cm$^{-1}$)')
ax.set_yticklabels([])
#plotting with shading
image = mpimg.imread('800px-Ethanolamine-2D-skeletal-B.png')
#read in image and make into array of colors
imagebox=OffsetImage(image, zoom=0.15)
ax.text(3250, 300, r'NH$_{2}$')
ax.text(3250,275, r'N-H')
ax.text(3210,250, r'Stretch')
ax.text(3170,570, r'3317')
ax.text(2850,300, r'CH$_{2}$')
ax.text(2850,275,r'C-H')
ax.text(2810,250,r'Stretch')
#rescaling size of image
structure = AnnotationBbox(imagebox,xy=(3300, 50),frameon=False)
#places image on plot at xy location
ax.add_artist(structure)
plt.tight_layout()
plt.savefig('MEAMFRamanwithstructure.png')
plt.show()