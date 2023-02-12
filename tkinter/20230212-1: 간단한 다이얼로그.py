"""
refer

http://pythonstudy.xyz/python/article/120-Tkinter-%EC%86%8C%EA%B0%9C
"""
from tkinter import *

root = Tk()
lable = Label(root, text="Hello, world!")
lable.grid(row=0,column=0) #pack은 상하로 정해진 위치 지정 방식, grid는 표처럼 지정하는 위치 지정 방식

txt = Entry(root)
txt.grid(row=0,column=1)

button = Button(root, text="OK", width=20)
button.grid(row=1,column=1)

root.mainloop()
