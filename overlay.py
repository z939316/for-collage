'''
3950
340 1899
'''
import cv2
import numpy as np
import time
path1 = 'F:/python/photo/overlay/1.jpg'
path2 = 'F:/python/photo/overlay/2.jpg'
path3 = 'F:/python/photo/overlay/3.jpg'
path4 = 'F:/python/photo/overlay/4.jpg'
img1 = cv2.imread(path1)
img2 = cv2.imread(path2)
img3 = cv2.imread(path3)
img4 = cv2.imread(path4)
endimg = cv2.imread(path4)
time0=time.time()
imga = cv2.addWeighted(img1,0.5,img2,0.5,0)
imgb = cv2.addWeighted(img3,0.5,img4,0.5,0)
endimg = cv2.addWeighted(imga,0.5,imgb,0.5,0)
print(time.time()-time0)
#shape = (img1.shape[0], img1.shape[1], img1.shape[2]) # y, x, RGB
#endimg = np.zeros(shape, np.uint8)
'''
for y in range(img1.shape[0]):
    if y%200 == 0:
        print(y)
    for x in range(img1.shape[1]):
        endimg[y][x][0] = (int(img1[y][x][0])+int(img2[y][x][0])+int(img3[y][x][0])+int(img4[y][x][0]))//4
        endimg[y][x][1] = (int(img1[y][x][1])+int(img2[y][x][1])+int(img3[y][x][1])+int(img4[y][x][1]))//4
        endimg[y][x][2] = (int(img1[y][x][2])+int(img2[y][x][2])+int(img3[y][x][2])+int(img4[y][x][2]))//4
        r=(int(img1[y][x][0])+int(img2[y][x][0])+int(img3[y][x][0])+int(img4[y][x][0]))//4
        g=(int(img1[y][x][1])+int(img2[y][x][1])+int(img3[y][x][1])+int(img4[y][x][1]))//4
        b=(int(img1[y][x][2])+int(img2[y][x][2])+int(img3[y][x][2])+int(img4[y][x][2]))//4
        endimg[y][x]=(r, g, b)
        '''

cv2.imwrite('print2.jpg',endimg)

    
'''
(0,1)
(3950,0.6928)
'''
