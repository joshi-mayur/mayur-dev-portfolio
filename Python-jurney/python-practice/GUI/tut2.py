#how to insert the JPG file
from tkinter import *
from PIL import Image, ImageTk  # <-- Import from Pillow for jpg format
root = Tk()

root.geometry("1250x1250")
#how to insert the png file

photo = PhotoImage(file="logo.png") 
label = Label(image=photo)
label.pack()


#for jpg inser
image = Image.open("hunter.jpg")
photo_2=ImageTk.PhotoImage(image)
label2 = Label(image=photo_2)

label2.pack()


root.mainloop()