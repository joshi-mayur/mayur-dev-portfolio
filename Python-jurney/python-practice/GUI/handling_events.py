from tkinter import *


def mayur(event):
    print(f"you clicked button at {event.x} , {event.y}")


root = Tk()
root.geometry("644x334")

widget = Button(root, text="click me please")
widget.pack()

#single click action
widget.bind('<Button-1>', mayur)

#doble click action please read the doc for the bind you will gett the more info
widget.bind('<Double-1>', quit)  #exit the code

root.mainloop()
