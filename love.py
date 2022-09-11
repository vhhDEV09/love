import tkinter
from tkinter import *
from tkinter.ttk import *
import time 
from time import sleep
sleep(1.4)
print("     Bat ngo lam dung hong")
sleep(1.4)
print("     Da vao day roi thi dung out nua=))")
sleep(1.4)
print("     Doi xiu")
sleep(1)
print("     3")
sleep(1)
print("     2")
sleep(1)
print("     1")
root = Tk()
root.geometry("1000x500")
root.title('Moving Text')

def MovingText(s):
    s1 = s[1:len(s)]
    s2 = s[0:1]
    string = s1 + s2
    label.config(text = string)
    label.after(100,MovingText,string)
label = Label(root, font = ('Time New Roman',50))
label.pack(anchor = 'center')
string = "Yêu em dúm s1tg 33" + '      '
MovingText(string)
root.mainloop()
