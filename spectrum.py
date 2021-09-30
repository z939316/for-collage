import numpy as np
import cv2

shape = (200, 763, 3) # y, x, RGB
img = np.zeros(shape, np.uint8)

for i in range(0,128):
    for r in range(200):
        img[r][i]=[0,i*2,254]
for i in range(128,255):
    for r in range(200):
        img[r][i]=[0,254,254-(i*2-254)]
for i in range(255,382):
    for r in range(200):
        img[r][i]=[i*2-508,254,0]
for i in range(382,509):
    for r in range(200):
        img[r][i]=[254,254-(i*2-762),0]
for i in range(509,636):
    for r in range(200):
        img[r][i]=[254,0,(i*2-1016)]
for i in range(636,763):
    for r in range(200):
        img[r][i]=[254-(i*2-1272),0,254]
print(img[r][i])
'''
cv2.imshow('My image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
cv2.imwrite('C:/Users/USER/Desktop/127,255,0.jpg',img)
