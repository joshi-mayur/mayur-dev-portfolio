from struct import pack_into
from tkinter import *
def click(event):
    global scvalue
    text = event.widget.cget("text")

    if text == "=":
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        else:
            value=eval(scvalue.get())
        scvalue.set(value)
        screen.update()

    elif text == "c":
        scvalue.set("")
        screen.update()

    else:
        scvalue.set(scvalue.get() + text)
        screen.update()



root = Tk()
root.geometry("300x550")
root.title("Calculator")
root.wm_iconbitmap("calculator_22694.ico")


scvalue = StringVar()
scvalue.set("")

screen = Entry(root, textvariable=scvalue, font=("Arial", 20,"bold"))
screen.pack(fill=X,ipady=10,padx=10, pady=10)

f1=Frame(root,bg="grey")
b1=Button(f1,text="9",padx=10,pady=10,font=("Arial",20,"bold"))
b1.pack(side=LEFT,padx=2,pady=2)
b1.bind("<Button-1>",click)

b2=Button(f1,text="8",padx=10,pady=10,font=("Arial",20,"bold"))
b2.pack(side=LEFT,padx=2,pady=2)
b2.bind("<Button-1>",click)

b3=Button(f1,text="7",padx=10,pady=10,font=("Arial",20,"bold"))
b3.pack(side=LEFT,padx=2,pady=2)
b3.bind("<Button-1>",click)

f1.pack()

f1=Frame(root,bg="grey")
b4=Button(f1,text="6",padx=10,pady=10,font=("Arial",20,"bold"))
b4.pack(side=LEFT,padx=2,pady=2)
b4.bind("<Button-1>",click)

b5=Button(f1,text="5",padx=10,pady=10,font=("Arial",20,"bold"))
b5.pack(side=LEFT,padx=2,pady=2)
b5.bind("<Button-1>",click)

b6=Button(f1,text="4",padx=10,pady=10,font=("Arial",20,"bold"))
b6.pack(side=LEFT,padx=2,pady=2)
b6.bind("<Button-1>",click)

f1.pack()

f1=Frame(root,bg="grey")

b7=Button(f1,text="3",padx=10,pady=10,font=("Arial",20,"bold"))
b7.pack(side=LEFT,padx=2,pady=2)
b7.bind("<Button-1>",click)

b7=Button(f1,text="2",padx=10,pady=10,font=("Arial",20,"bold"))
b7.pack(side=LEFT,padx=2,pady=2)
b7.bind("<Button-1>",click)

b8=Button(f1,text="1",padx=10,pady=10,font=("Arial",20,"bold"))
b8.pack(side=LEFT,padx=2,pady=2)
b8.bind("<Button-1>",click)
f1.pack()

f1=Frame(root,bg="grey")

b7=Button(f1,text="+",padx=10,pady=10,font=("Arial",20,"bold"))
b7.pack(side=LEFT,padx=2,pady=2)
b7.bind("<Button-1>",click)

b7=Button(f1,text="-",padx=10,pady=10,font=("Arial",20,"bold"))
b7.pack(side=LEFT,padx=2,pady=2)
b7.bind("<Button-1>",click)

b8=Button(f1,text="*",padx=10,pady=10,font=("Arial",20,"bold"))
b8.pack(side=LEFT,padx=2,pady=2)
b8.bind("<Button-1>",click)
f1.pack()

f1=Frame(root,bg="grey")

b7=Button(f1,text="/",padx=10,pady=10,font=("Arial",20,"bold"))
b7.pack(side=LEFT,padx=2,pady=2)
b7.bind("<Button-1>",click)

b7=Button(f1,text="%",padx=10,pady=10,font=("Arial",20,"bold"))
b7.pack(side=LEFT,padx=2,pady=2)
b7.bind("<Button-1>",click)

b8=Button(f1,text="c",padx=10,pady=10,font=("Arial",20,"bold"))
b8.pack(side=LEFT,padx=2,pady=2)
b8.bind("<Button-1>",click)
f1.pack()

f1=Frame(root,bg="grey")

b7=Button(f1,text="=",padx=10,pady=10,font=("Arial",20,"bold"))
b7.pack(side=LEFT,padx=2,pady=2)
b7.bind("<Button-1>",click)
f1.pack()


root.mainloop()