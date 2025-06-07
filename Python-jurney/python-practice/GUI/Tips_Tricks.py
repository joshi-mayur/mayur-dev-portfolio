from tkinter import *
root = Tk()
root.geometry("655x444")
root.title("Tips Tricks")

root.wm_iconbitmap("logo.ico") #your GUI icon
root.configure(bg="black") # bg means background

width=root.winfo_screenwidth() #to get your screen width
height=root.winfo_screenheight() #to get your screen width

print(f"{width}x{height}")

Button(text="close",command=root.destroy).pack() #to close your GUI

root.mainloop()