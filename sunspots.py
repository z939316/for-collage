from PIL import Image, ImageDraw
import requests
import urllib.request
import time
import cv2
import glob
fps =60

fourcc = cv2.VideoWriter_fourcc(*'MP4V')
videoWriter = cv2.VideoWriter('sunspots60.mp4',fourcc,fps,(1024,1024))
# open the file using open()
imgname=[]
count=0
headers = {
    'User-Agent': 'My User Agent 1.0'
}
#file=open("index.txt",'r',encoding="utf-8")
with open("index.txt",mode="r",encoding="utf-8") as file:
    for line in file:
        line=line.split()
        imgname.append(line[0])


print(len(imgname))
for i in range(100): 
    url='https://sohowww.nascom.nasa.gov/data/synoptic/sunspots_earth/'+imgname[i]
    time2=time.time()
    img_data = requests.get(url,headers).content
    time3=time.time()
    count+=time3-time2
    print("time",time3-time2)
    with open('%s/%s' % ("F:/sunspots/img", imgname[i]), 'wb') as f:
        f.write(img_data)
    frame = cv2.imread('F:/sunspots/img/'+imgname [i])
    videoWriter.write(frame)
    print(imgname[i])
print(count/10)
videoWriter.release()

