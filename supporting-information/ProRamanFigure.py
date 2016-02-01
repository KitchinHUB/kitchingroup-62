import xlrd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
#reading in data
wb = xlrd.open_workbook('RawData.xlsx')
sh1=wb.sheet_by_name(u'ProRaman')
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
ax.set_ylim(0, 120)
ymax = ax.get_ylim()[1] + ax.get_ylim()[0]
ax.fill_between(xpf[shadeu], y1=np.zeros(len(xpf[shadeu])),y2=ymax*np.ones(len(xpf[shadeu])),
                color='#C8C8C8')
shadei= (xpf>800) & (xpf<1000)

ax.fill_between(xpf[shadei],y1=np.zeros(len(xpf[shadei])),y2=ymax*np.ones(len(xpf[shadei])),color='#B8B8B8')
shadeo= (xpf>1130) & (xpf<1190)
ax.fill_between(xpf[shadeo],y1=np.zeros(len(xpf[shadeo])),y2=ymax*np.ones(len(xpf[shadeo])),color='#B0B0B0')
ax.plot(xf,yf, label='Post-MF expt')#plotting post data
ax.set_xlim([800,1800])
ax.legend(loc='upper right')
ax.text(1450,16,r'CO$_{2}$$^{-}$')
ax.text(1410,12,r'Stretch')
ax.text(1410,8,r'R$_{1}$R$_{2}$NH')
ax.text(1450,4,r'N-H')
ax.text(1410,0.5,r'Stretch')
ax.text(1275,75,r'1350')
ax.text(1310,79,r'$\bigstar$',color='r')
ax.text(1070,14,r'R$_{1}$R$_{2}$NH')
ax.text(1093,10,r'C-N-C')
ax.text(1080,6,r'Stretch')
ax.text(850,20,r'CH$_{2}$')
ax.text(840,16,r'Twist')
ax.text(845,11,r'CCO')
ax.text(820,7,r'Stretch')
ax.text(1630,95,r'HCO$_{3}$$^{-}$',color='r')
ax.text(1592,96,r'$\bigstar$',color='r')
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

shadeq = (xph>2800) & (xph< 3000)
ax.fill_between(xph[shadeq],y1=np.zeros(len(xph[shadeq])),y2=ymax*np.ones(len(xph[shadeq])), color='#A8A8A8')                
ax.plot(xh,yh, label='Post-MF expt')
ax.set_xlim([2800,3800])
ax.text(2850,400,r'CH$_{2}$')
ax.text(2850,370,r'C-H')
ax.text(2810,350,r'Stretch')
ax.set_xlabel('Wavenumber (cm$^{-1}$)')
ax.set_yticklabels([])
#text + image
image = mpimg.imread('Proline.png')
#read in image and make into array of colors
imagebox=OffsetImage(image, zoom=0.8)
#rescaling size of image
structure = AnnotationBbox(imagebox,xy=(3300, 100),frameon=False)
#places image on plot at xy location
ax.add_artist(structure)
plt.tight_layout()
plt.savefig('PROMFRamanwithstructure.png')
plt.show()
