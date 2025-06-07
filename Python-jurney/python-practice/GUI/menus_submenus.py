#Creating menu and submenu 
from tkinter import *
root = Tk()
root.geometry('700x566')
def myfunc():
    print("Goog keep going !")

mainmenu = Menu(root)
m1=Menu(mainmenu, tearoff=0)
m1.add_command(label="new Porject",command=myfunc)
m1.add_command(label="Save",command=myfunc)
m1.add_command(label="Save As",command=myfunc)
m1.add_separator()
m1.add_command(label="Exit",command=root.quit)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="File", menu=m1)

m1=Menu(mainmenu, tearoff=0)
m1.add_command(label="Copy",command=myfunc)
m1.add_command(label="Cut",command=myfunc)
m1.add_separator()
m1.add_command(label="Find",command=myfunc)

mainmenu.add_cascade(label="Edit", menu=m1)

root.mainloop()

