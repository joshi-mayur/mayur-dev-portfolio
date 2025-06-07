#creating Scroll bar
from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.geometry('700x566')
root.title("Scroll Bar")

#for conneting scroll bar to a widget
# 1 . widget(yscrollcommand = scrollbar.set)
#2. scrollbar.config(command=widget.yview)

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)

listbox = Listbox(root,yscrollcommand=scrollbar.set)
for i in range(100):
    listbox.insert(END,f"{i}")

listbox.pack(fill="both")
scrollbar.config(command=listbox.yview)
root.mainloop()
