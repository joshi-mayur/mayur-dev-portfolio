from tkinter import *
root = Tk()
def getvals():
    print(user_value.get())
    print(passoword_value.get())


#Width X height
root.geometry("444x234")


user = Label(root,text="username")
pass_word = Label(root,text="Password")
user.grid()
pass_word.grid(row=1)

user_value = StringVar()
passoword_value = StringVar()


user_entry=Entry(root,textvariable=user_value)
pass_entry=Entry(root,textvariable=passoword_value)

user_entry.grid(row=0,column=1)
pass_entry.grid(row=1,column=1)

b1=Button(text="Submit",command=getvals).grid()


root.mainloop()
