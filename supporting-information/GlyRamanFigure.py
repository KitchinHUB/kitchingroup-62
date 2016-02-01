import xlrd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
#reading in data
wb = xlrd.open_workbook('RawData.xlsx')
sh1=wb.sheet_by_name(u'GlyRaman')
xf=sh1.col_values(3) #wavenumber
yf=sh1.col_values(5) #Raman intensity postMF fingerprint region
xpf=sh1.col_values(0)
ypf=sh1.col_values(1)# Raman intensity preMF fingerprint region
xh=sh1.col_values(9,end_rowx=2583)
yh=sh1.col_values(10,end_rowx=2583)#Raman intensity postMF high region
xph=sh1.col_values(6,end_rowx=2583)
yph=sh1.col_values(7,end_rowx=2583)#Raman intensity preMF high region
#creating Figure
fig=plt.figure()
#adding left subplot
ax = fig.add_subplot(1,2,1)
ax.plot(xpf,ypf, label='Pre-MF expt')  # plotting pre data
#making shading
xpf = np.array(xpf)
ypf = np.array(ypf)
shadeu = (xpf > 1400) & (xpf < 1600)
ax.set_ylim(5, 100)
ymax = ax.get_ylim()[1] + ax.get_ylim()[0]
ax.fill_between(xpf[shadeu], y1=np.zeros(len(xpf[shadeu])),y2=ymax*np.ones(len(xpf[shadeu])),
                color='#C8C8C8')
shadei= (xpf>800) & (xpf<1000)

ax.fill_between(xpf[shadei],y1=np.zeros(len(xpf[shadei])),y2=ymax*np.ones(len(xpf[shadei])),color='#B8B8B8')
ax.plot(xf,yf, label='Post-MF expt')#plotting post data
ax.set_xlim([800,1800])
ax.legend(loc='upper right')
ax.text(1450,14,r'CO$_{2}$$^{-}$')
ax.text(1410,10,r'Stretch')
ax.text(1430,57,r'1445')
ax.text(1135,51,r'1175')
ax.text(1140,54,r'$\bigtriangleup$',color='r')
ax.text(990,71,r'1045')
ax.text(1010,74,r'$\bigstar$',color='r')
ax.text(1000,77,r'$\bigcirc$',color='r')
ax.text(900,80,r'914')
ax.text(850,22,r'CH$_{2}$')
ax.text(835,19,r'Twist')
ax.text(850,16,r'CCO')
ax.text(820,13,r'Stretch')
ax.text(1500,83,r'Carbamate',color='r')
ax.text(1430,83,r'$\bigtriangleup$',color='r')
ax.text(1440,79,r'$\bigstar$',color='r')
ax.text(1500,79,r'HCO$_{3}$$^{-}$',color='r')
ax.text(1430,75,r'$\bigcirc$',color='r')
ax.text(1500,75,r'CO$_{3}$$^{-2}$',color='r')
ax.set_xlabel('Wavenumber (cm$^{-1}$)')
ax.set_ylabel('Raman Intensity (a.u.)')
ax.set_yticklabels([])
#adding subplot two
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
ax.text(3250,400,r'NH$_{2}$')
ax.text(3250,370,r'N-H')
ax.text(3210,345,r'Stretch')
ax.text(3245,556,r'3320')
ax.text(2850,400,r'CH$_{2}$')
ax.text(2850,370,r'C-H')
ax.text(2810,345,r'Stretch')
image = mpimg.imread('glycine.png')
#read in image and make into array of colors
imagebox=OffsetImage(image, zoom=0.8)
#rescaling size of image
structure = AnnotationBbox(imagebox,xy=(3300, 100),frameon=False)
#places image on plot at xy location
ax.add_artist(structure)
plt.tight_layout()
plt.savefig('GLYMFRamanwithstructure.png')
plt.show()