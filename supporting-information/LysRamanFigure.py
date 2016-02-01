import xlrd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
#reading in data
wb = xlrd.open_workbook('RawData.xlsx')
sh1=wb.sheet_by_name(u'LysRaman')
xpf=sh1.col_values(0) #wavenumber
ypf=sh1.col_values(1) #Raman intensity preMF fingerprint region
xf=sh1.col_values(3)
yf=sh1.col_values(5)#Raman intensity postMF fingerprint region
xph=sh1.col_values(9,end_rowx=2583)
yph=sh1.col_values(10,end_rowx=2583)#Raman intensity preMF high region
xh=sh1.col_values(6,end_rowx=2583)
yh=sh1.col_values(7,end_rowx=2583)#Raman intensity postMF high region
#creating Figure
fig=plt.figure()
#adding left subplot
ax = fig.add_subplot(1,2,1)
ax.plot(xpf,ypf, label='Pre-MF expt')  # plotting pre data
#making shading
xpf = np.array(xpf)
ypf = np.array(ypf)
shadeu = (xpf > 1400) & (xpf < 1600)
ax.set_ylim(10, 120)
ymax = ax.get_ylim()[1] + ax.get_ylim()[0]
ax.fill_between(xpf[shadeu], y1=np.zeros(len(xpf[shadeu])),y2=ymax*np.ones(len(xpf[shadeu])),
                color='#C8C8C8')
shadei= (xpf>800) & (xpf<1000)

ax.fill_between(xpf[shadei],y1=np.zeros(len(xpf[shadei])),y2=ymax*np.ones(len(xpf[shadei])),color='#B8B8B8')

ax.plot(xf,yf, label='Post-MF expt')#plotting post data
ax.set_xlim([800,1800])
ax.legend(loc='upper right')
ax.text(1450,25,r'CO$_{2}$$^{-}$')
ax.text(1410,21,r'Stretch')
ax.text(1100,80,r'1130')
ax.text(1100,83,r'$\bigtriangleup$',color='r')
ax.text(1030,106,r'1068')
ax.text(1030,110,r'$\bigcirc$',color='r')
ax.text(930,96.5,r'1017')
ax.text(992,100,r'$\bigstar$',color='r')
ax.text(850,40,r'CH$_{2}$')
ax.text(830,36,r'Twist')
ax.text(850,28,r'CCO')
ax.text(820,24,r'Stretch')
ax.text(1510,100,r'Carbamate',color='r')
ax.text(1450,100,r'$\bigtriangleup$',color='r')
ax.text(1460,95,r'$\bigstar$',color='r')
ax.text(1510,95,r'HCO$_{3}$$^{-}$',color='r')
ax.text(1450,90,r'$\bigcirc$',color='r')
ax.text(1510,90,r'CO$_{3}$$^{-2}$',color='r')
ax.set_xlabel('Wavenumber (cm$^{-1}$)')
ax.set_ylabel('Raman Intensity (a.u.)')
ax.set_yticklabels([])
#adding subplot two
ax = fig.add_subplot(1,2,2)
ax.plot(xph,yph, label='Pre-MF expt')
#making shading
xph = np.array(xph)
yph = np.array(yph)
ax.set_ylim(0,800)
ymax = ax.get_ylim()[1]+ax.get_ylim()[0]

shadeq = (xph>2800) & (xph< 3000)
ax.fill_between(xph[shadeq],y1=np.zeros(len(xph[shadeq])),y2=ymax*np.ones(len(xph[shadeq])), color='#A8A8A8')  
shadey= (xph>3200) &(xph<3400)
ax.fill_between(xph[shadey],y1=np.zeros(len(xph[shadey])),y2=ymax*np.ones(len(xph[shadey])), color= '#A0A0A0')              
ax.plot(xh,yh, label='Post-MF expt')
ax.set_xlim([2800,3800])
ax.set_xlabel('Wavenumber (cm$^{-1}$)')
ax.set_yticklabels([])
#text+image
ax.text(3250,400,r'NH$_{2}$')
ax.text(3250,370,r'N-H')
ax.text(3210,350,r'Stretch')
ax.text(3250,730,r'3310')
ax.text(2850,400,r'CH$_{2}$')
ax.text(2850,370,r'C-H')
ax.text(2810,350,r'Stretch')
image = mpimg.imread('Lysine.png')
#read in image and make into array of colors
imagebox=OffsetImage(image, zoom=0.65)
#rescaling size of image
structure = AnnotationBbox(imagebox,xy=(3320, 75),frameon=False)
#places image on plot at xy location
ax.add_artist(structure)
plt.tight_layout()
plt.savefig('LYSMFRamanwithstructure.png')
plt.show()
