import xlrd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
#reading in data
wb = xlrd.open_workbook('RawData.xlsx')
sh1=wb.sheet_by_name(u'TauRaman')
xpf=sh1.col_values(0) #wavenumber
ypf=sh1.col_values(1) #Raman intensity preMF fingerprint region
xf=sh1.col_values(3)
yf=sh1.col_values(5) #Raman intensity postMF fingerprint region
xph=sh1.col_values(6,end_rowx=2583)
yph=sh1.col_values(7,end_rowx=2583)#Raman intensity preMF high region
xh=sh1.col_values(9,end_rowx=2583)
yh=sh1.col_values(10,end_rowx=2583)#Raman intensity postMF high region
#Creating figure
fig=plt.figure()
#adding left subplot
ax = fig.add_subplot(1,2,1)
ax.plot(xpf,ypf, label='Pre-MF expt')  # plotting pre data
#making shading
xpf = np.array(xpf)
ypf = np.array(ypf)
shadeu = (xpf > 1400) & (xpf < 1600)
ax.set_ylim(0, 400)
ymax = ax.get_ylim()[1] + ax.get_ylim()[0]
ax.fill_between(xpf[shadeu], y1=np.zeros(len(xpf[shadeu])),y2=ymax*np.ones(len(xpf[shadeu])),
                color='#C8C8C8')
shadei= (xpf>700) & (xpf<1000)

ax.fill_between(xpf[shadei],y1=np.zeros(len(xpf[shadei])),y2=ymax*np.ones(len(xpf[shadei])),color='#B8B8B8')
shadee= (xpf>1030) & (xpf<1070)
ax.fill_between(xpf[shadee],y1=np.zeros(len(xpf[shadee])),y2=ymax*np.ones(len(xpf[shadee])),color='#C0C0C0')

ax.plot(xf,yf, label='Post-MF expt')#plotting post data
ax.set_xlim([700,1700])
ax.legend(loc='upper right')
ax.text(1450,100,r'CO$_{2}$$^{-}$')
ax.text(1410,85,r'Stretch')
ax.text(1280,60,r'1340')
ax.text(1310,72,r'$\bigstar$',color='r')
ax.text(1020,250,r'SO$_{3}$$^{-}$')
ax.text(1020,230,r'Stretch')
ax.text(900,80,r'955')
ax.text(800,300,r'CH$_{2}$')
ax.text(800,285,r'Twist')
ax.text(800,270,r'CCO')
ax.text(800,255,r'Stretch')
ax.text(1530,300,r'HCO$_{3}$$^{-}$',color='r')
ax.text(1480,300,r'$\bigstar$',color='r')
ax.set_xlabel('Wavenumber (cm$^{-1}$)')
ax.set_ylabel('Raman Intensity (a.u.)')
ax.set_yticklabels([])
#adding second subplot
ax = fig.add_subplot(1,2,2)
ax.plot(xph,yph, label='Pre-MF expt')
#making shading
xph = np.array(xph)
yph = np.array(yph)
ax.set_ylim(0,700)
ymax = ax.get_ylim()[1]+ax.get_ylim()[0]
shadex = (xph > 3200) & (xph < 3400)
ax.fill_between(xph[shadex], y1=np.zeros(len(xph[shadex])),y2=ymax*np.ones(len(xph[shadex])),
                color='#D0D0D0')
shadeq = (xph>2800) & (xph< 3000)
ax.fill_between(xph[shadeq],y1=np.zeros(len(xph[shadeq])),y2=ymax*np.ones(len(xph[shadeq])), color='#A8A8A8')                
ax.plot(xh,yh, label='Post-MF expt')
ax.set_xlim([2800,3800])

ax.set_xlabel('Wavenumber (cm$^{-1}$)')
ax.set_yticklabels([])
#text+image
ax.text(3250,300,r'NH$_{2}$')
ax.text(3250,270,r'N-H')
ax.text(3210,250,r'Stretch')
ax.text(3270,560,r'3317')
ax.text(2850,300,r'CH$_{2}$')
ax.text(2850,270,r'C-H')
ax.text(2810,250,r'Stretch')
image = mpimg.imread('Taurine.png')
#read in image and make into array of colors
imagebox=OffsetImage(image, zoom=0.4)
#rescaling size of image
structure = AnnotationBbox(imagebox,xy=(3300, 90),frameon=False)
#places image on plot at xy location
ax.add_artist(structure)
plt.tight_layout()
plt.savefig('TauMFRamanwithstructure.png')
plt.show()