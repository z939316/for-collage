import numpy as np
import cv2
import random
import time
s=1
t=time.time()
shape = (10000, 10000, 3) # y, x, RGB
img = np.zeros(shape, np.uint8)
'''
for i in range(0,1000,s):
    for r in range(0,1000,s):
        a=random.randint(0,255)
        b=random.randint(0,255)
        c=random.randint(0,255)
        for x in range(s):
            for y in range(s):
                img[r+x][i+y]=[a,a,a]
'''
for i in range(0,10000):
    if int(time.time()-t)%50==0:
        print(i)
    for r in range(0,10000):
        img[r][i]=[random.randint(0,255),random.randint(0,255),random.randint(0,255)]
cv2.imwrite('C:/Users/USER/Desktop/8KKK.jpg',img)
print(time.time()-t)

