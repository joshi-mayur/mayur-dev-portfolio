from tkinter import *

root = Tk()
root.geometry("800x400")

can_widget = Canvas(root, width=800, height=400)
can_widget.pack()

#The line goes from the point x1 y1 x2 y2
can_widget.create_line(0, 0, 800, 400, fill="red")
can_widget.create_line(0, 400, 800, 0, fill="blue")

#TO create a rectangle specify parameters in this order - coordinates of top left and coors of bottom right
can_widget.create_rectangle(3, 5, 700, 300)
can_widget.create_text(200,200,text="python zindabad")



root.mainloop()
