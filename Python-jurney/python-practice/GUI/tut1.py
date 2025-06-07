#how to lock the size of GUI
from tkinter import *
root = Tk()

#Width X height
root.geometry("444x234")

#width , height
root.minsize(200,100)

#width , height
root.maxsize(500,500)

label_name = Label(text="My GUI tutorial")
label_name.pack()  


root.mainloop()

