#creating slider 
from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.geometry('700x566')
root.title("Sliders")

def getdoller():
    tmsg.showinfo("Amount credited!",f"{myslider2.get()} dollar credited")

Label(root,text="How many dollars do you want ?").pack()
myslider2=Scale(root, from_=0, to=100, orient=HORIZONTAL,tickinterval=50)
myslider2.set(50)

myslider2.pack()

Button(root,text="Get dollars",command=getdoller).pack()

root.mainloop()