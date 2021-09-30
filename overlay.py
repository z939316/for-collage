import cv2
import numpy as np
path1 = 'F:/python/photo/overlay/1.jpg'
path2 = 'F:/python/photo/overlay/2.jpg'
path3 = 'F:/python/photo/overlay/3.jpg'
path4 = 'F:/python/photo/overlay/4.jpg'
img1 = cv2.imread(path1)
img2 = cv2.imread(path2)
img3 = cv2.imread(path3)
img4 = cv2.imread(path4)
endimg = cv2.imread(path4)
imga = cv2.addWeighted(img1,0.5,img2,0.5,0)
imgb = cv2.addWeighted(img3,0.5,img4,0.5,0)
endimg = cv2.addWeighted(imga,0.5,imgb,0.5,0)
cv2.imwrite('print2.jpg',endimg)

