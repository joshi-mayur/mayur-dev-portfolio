#creating messagebox
rom tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.geometry('700x566')
def myfunc():
    print("Goog keep going !")
def help():
    value=tmsg.showinfo("Help","Joshi will help you !")
    print(value)
def rate():
    value=tmsg.askquestion("was your experience Good ?","You used this gui..was your experience Good ?")
    tmsg.showinfo("your experience Noted ","your experience Noted ")

def divya():
    ans=tmsg.askokcancel("Divya se dosti kar lo","Sorry divya nahi banegi aapki dost")
    if ans:
        print("bhai  kuch nai hole vala ")
    else :
        print("vese bhi kuch nai hota")
mainmenu = Menu(root)
m1=Menu(mainmenu, tearoff=0)
m1.add_command(label="new Porject",command=myfunc)
m1.add_command(label="Save",command=myfunc)
m1.add_command(label="Save As",command=myfunc)
m1.add_separator()
m1.add_command(label="Exit",command=root.quit)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="File", menu=m1)

m2=Menu(mainmenu, tearoff=0)
m2.add_command(label="Copy",command=myfunc)
m2.add_command(label="Cut",command=myfunc)
m2.add_separator()
m2.add_command(label="Find",command=myfunc)

mainmenu.add_cascade(label="Edit", menu=m2)

m3=Menu(mainmenu, tearoff=0)
m3.add_command(label="Help",command=help)
m3.add_command(label="Rate us",command=rate)
m3.add_separator()
m3.add_command(label="Befriend Divya",command=divya)

mainmenu.add_cascade(label="Help", menu=m3)
root.config(menu=mainmenu)


root.mainloop()

