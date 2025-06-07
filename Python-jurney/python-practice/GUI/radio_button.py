#Creating a radio button
from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.geometry('700x566')
root.title("radio button")

def order():
    tmsg.showinfo("Order", f"you selected {var.get()} food ")

var = IntVar()

Label(root, text="select your food", padx=5, pady=5).pack()

radio = Radiobutton(root,text="veg",padx=14, variable=var, value=1).pack(anchor="w")
radio = Radiobutton(root,text="Non veg",padx=14, variable=var, value=2).pack(anchor="w")
radio = Radiobutton(root,text="sea food",padx=14, variable=var, value=3).pack(anchor="w")

Button(root,text="Show menu",command=order).pack()


root.mainloop()
