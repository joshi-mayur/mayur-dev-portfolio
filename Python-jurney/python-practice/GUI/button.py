from tkinter import *
def check():
    print("welcome to GUI")

def Name():
    print("my name is joshi")


root =Tk()
root.geometry("655x333")
f1= Frame(root,borderwidth=9,bg="gray",relief=SUNKEN)
f1.pack(side=LEFT,anchor="nw")

b1=Button(f1, fg="red", text="check",command=check)
b1.pack(side=LEFT, padx=3)

b2=Button(f1, fg="red", text="Name",command=Name)
b2.pack(side=LEFT, padx=3)

b3=Button(f1,fg="red", text="Run3")
b3.pack(side=LEFT, padx=3)

b4=Button(f1, fg="red", text="Run4")
b4.pack(side=LEFT, padx=3)


root.mainloop()