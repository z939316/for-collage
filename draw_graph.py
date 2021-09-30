import matplotlib
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties


import numpy as np

#fig = plt.figure(figsize=(8,4))#圖片輸出比例？大小？

X=np.arange(0,12.1,0.1)
Y=X**2

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False
# 上面這兩句有設應該就行了

#plt.plot(X,Y)
#plt.plot(X,Y,'r--')#紅，虛線
#plt.plot(X,Y,'r:')#紅，點+虛線
#plt.plot(X,Y,'r-.')#紅，線+點
plt.plot(X, Y, color='lime', linestyle='-', linewidth=10, alpha = 0.4, \
    marker='v', markerfacecolor='black',markeredgecolor='red', \
         markersize=4,markeredgewidth=1, label='n=2', zorder=2)#linestyle=''無線
#alpha透明度，越小越透明
plt.plot(X, X**2.2, color='yellow', linestyle='-', linewidth=10, \
    marker='v', markerfacecolor='black',markeredgecolor='red', \
         markersize=4,markeredgewidth=1, label='n=2.2', zorder=1)#zorder=>圖層
axl = plt.gca()
axl.set_title("I am groot",fontname='Arial',fontsize=20, \
              weight='bold', style='italic')
axl.set_xlabel('X')
axl.set_ylabel('X$^n$')

axl.set_xticks([0,2.5,7,11])
axl.set_xticklabels(['零','貳點伍','柒','拾壹'])
axl.tick_params(axis='both',direction='inout',color='black', \
                length=10, width=2)#axix=both or x or y
plt.legend(loc='upper right')#best upper right lower left center left lower center
plt.savefig('./print.png')
'''
#畫多圖
fig, ax = plt.subplots(2,1)
ax[0].plot(X,Y)
ax[1].plot(X,X**2)
ax[0].set_xlim([0,10])
ax[1].set_xlim([0,10])
'''
'''
#指數軸
X2 = np.arange(1,100,1)
Y2 = np.exp(X2)
plt.plot(X2,Y2)
ax = plt.gca()
ax.set_yscale('log')
#左右上下軸
ax2 = ax.twinx()
#ax2.plot(X,Y,'ro')
ax3 = ax2.twiny()
ax3.plot(X,Y,'ro')
'''
fig1= plt.gcf()
#plt.tight_layout()#確保圖不會被割
#plt.show()
fig1.savefig('printdpi2000g.png',dpi=2000)
