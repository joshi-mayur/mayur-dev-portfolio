from tkinter import *

root = Tk()
root.geometry("655x333")
f1 = Frame(root, bg="grey", borderwidth=6, relief=SUNKEN)
f1.pack(side=LEFT, fill="y")  # if stretch the GUI it will remain same

l = Label(f1, text="Project Tkinter - Editor")
l.pack(pady=142)  # your text stay in middle


#lets make another frame in top of GUI

f2=Frame(root,bg="gray", borderwidth=8,relief=SUNKEN)
f2.pack(side=TOP, fill="x")

l2=Label(f2, text="My editor",font="Helvetica 16 bold",fg="red")
l2.pack(pady=10)

root.mainloop()

