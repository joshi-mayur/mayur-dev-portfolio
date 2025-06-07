#how to create the status bar 
from tkinter import *

def upload():
    statusvar.set("Busy")
    statusbar.update()
    import time
    time.sleep(2)
    statusvar.set("Ready")

root = Tk()
root.geometry("300x300")
root.title("Status bar tutorial")

statusvar = StringVar()
statusvar.set("Ready")
statusbar = Label(root, textvariable=statusvar, relief=SUNKEN, anchor=W)
statusbar.pack(side=BOTTOM, fill=X)
Button(root, text="Upload", command=upload).pack()
root.mainloop()