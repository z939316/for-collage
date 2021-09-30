#!/usr/bin/env python
'''
import tkinter as tk
window = tk.Tk()
window.title('pi camera test')
window.geometry('600x800')
lbl_1 = tk.Label(window, text='Hello World', bg='yellow', fg='#263238', font=('Arial', 12))
lbl_1.grid(column=0, row=0)
window.mainloop()
'''
from tkinter import*
#from PIL import Image, ImageTk
import pyperclip
import  ImageTk, Image, ImageDraw

win = Tk()
win.title("test")
win.geometry('800x600+850+150')
win.minsize(width = 400, height = 300)
win.maxsize(width = 1600, height = 1200)
win.config(background="#323232")
win.attributes("-alpha",1)#0~1#透明度
win.attributes("-topmost",1)#置頂開啟

def say_hi():
    print("讓我看看")
'''
def ok():
    t = en.get()
    lb.config(text=t)
    lb.pack_forget()
    #shoot.pack()
    '''
def number():
    n.pack_forget()
    s.pack_forget()
    f.pack_forget()
    nlb.pack()
    nen.pack()
    nok.pack()
    nbabn.pack()
def numberok():
    t = nen.get()
    numberback()
def numberback():
    n.pack()
    s.pack()
    f.pack()
    nok.pack_forget()
    nlb.pack_forget()
    nen.pack_forget()
    nbabn.pack_forget()
def ge():
    if scv.get():
        print("大膽！")
    else:
        print("我的9.2真乖")
def shoot():
    n.pack_forget()
    s.pack_forget()
    f.pack_forget()
    #img=PhotoImage(file="C:/Users/USER/Pictures/12345.png")
    #slb= Label(height=36,width=48,bg ='gray94',fg='blue',image = img) 
    slb.pack()
    ss.place(anchor=NW,x=0,y=200,width=150,height=150)
    sbabn.place(x=0,y=0,width=150,height=150)
    sc.pack()
    
    
def shootback():
    #img=PhotoImage(file="C:/Users/USER/Pictures/12345.png")
    #slb= Label(height=36,width=48,bg ='gray94',fg='blue',image = img)
    slb.pack_forget()
    sbabn.place_forget()
    ss.place_forget()
    sc.pack_forget()
    n.pack()
    s.pack()
    f.pack()

def focus():
    n.pack_forget()
    s.pack_forget()
    f.pack_forget()
def copy():
    pyperclip.copy("哈哈哈")
#win.resizable(0, 0)#禁止縮放
#icopath=""
#win.iconbitmap(icopath)

#lb=Label(bg="#323232",fg="white",text="我是新細明體，打我啊！")
#lb.config(font="新細明體 20")
#lb.pack()

#en=Entry()
#en.pack()



img=PhotoImage(file="C:/Users/USER/Pictures/12345.png")
#連拍數
n=Button(text="連拍數", bg="skyblue",width=8,height=2,font="MStiffHeiHK-UltraBold 40",command= number)
nlb=Label(bg="#323232",fg="white",text="快講要拍幾張啦！",width=20,height=2,font="MStiffHeiHK-UltraBold 30")
nen=Entry(font="MStiffHeiHK-UltraBold 40",fg='black')
#nen.insert(0, "請輸入數字")
nok=Button(text="就這麼多張", bg="skyblue",width=8,height=2,font="MStiffHeiHK-UltraBold 40",command= numberok)
nbabn=Button(text="返回", bg="skyblue",width=8,height=2,font="MStiffHeiHK-UltraBold 40",command= numberback)

                 

s=Button(text="拍攝", bg="skyblue",width=8,height=2,font="MStiffHeiHK-UltraBold 40",command= shoot)
sbabn=Button(text="返回", bg="skyblue",width=8,height=3,font="MStiffHeiHK-UltraBold 40",command= shootback)
slb=Label(text="拍攝", bg="skyblue",width=185,height=200,image=img)
ss=Scale(orient=HORIZONTAL,width=100,length=200,from_=1,to=10,bg="#323232",fg='white')
ss.config(showvalue=1,tickinterval=2,resolution=0.25,digits=3)
ss.set(4.5)
scv = IntVar()
sc = Checkbutton(text = "乳馬", variable = scv, \
                 onvalue = 1, offvalue = 0, height=1, \
                 width = 4,highlightcolor='skyblue',command=ge, \
                 bg='#323232', activebackground='white',font="MStiffHeiHK-UltraBold 40")

f=Button(text="焦距", bg="skyblue",width=8,height=3,font="MStiffHeiHK-UltraBold 40",command= focus)
#slb=Label(bg="#323232",fg="white",text="快講要拍幾張啦！",font="微軟正黑體 20")
#sen=Entry()
#sok=Button(text="就這麼多張", bg="skyblue",width=20,height=10,command= numberok)
#btn.config(bg="skyblue")#獨立出來
#btn.config(image=img)
#btn.config(command=say_hi)

n.pack()
s.pack()
f.pack()
#n.grid(row=0,column=0)
#s.grid(row=0,column=1,rowspan=2)
#f.grid(row=1,column=0)
#n.place(anchor=NW,x=0,y=0,width=400,height=400)#anchor=N NE E SE S SW W NW CENTER
#s.place(x=400,y=0)
#f.place(x=0,y=300)
#f.place_forget()

win.mainloop()
