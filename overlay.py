import cv2
import numpy as np
import time
import os
n=0
path=os.path.dirname(os.path.abspath(__file__))
listimg=[]
for filename in os.listdir(path): 
    if "jpg" not in filename and "png" not in filename:     
        continue
    n+=1
    globals()[filename] = cv2.imread(filename)
    listimg.append(filename)
printimg=globals()[listimg[0]]
printimg=cv2.addWeighted(globals()[listimg[0]],0.5,globals()[listimg[1]],0.5,0)

if n>2:
    for i in range(len(listimg)-2):
        printimg=cv2.addWeighted(printimg,(i+2)/(i+3),globals()[listimg[i+2]],1-(i+2)/(i+3),0)
cv2.imwrite('print100.jpg',printimg) 

