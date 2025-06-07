from tkinter import *

def add():
    global i
    lbx.insert(ACTIVE, f"{i}") #Active means nex value added from there
    i+=1
i=0

root=Tk()
root.geometry("300x300")
root.title("List box")

lbx=Listbox(root)
lbx.pack()
lbx.insert(ACTIVE, f"{i}")

Button(root,text="Add Item",command=add).pack()
root.mainloop()