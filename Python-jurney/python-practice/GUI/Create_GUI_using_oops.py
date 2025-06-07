from tkinter import *

class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("800x600")
        self.title("Creating GUI using class")

    def status(self):
        self.var = StringVar()
        self.var.set("Ready")
        self.statusbar = Label(self, textvariable=self.var, relief=SUNKEN, anchor=W).pack(side=BOTTOM, fill=X)
    def clicked(self):
        pass
    def createbutton(self,input_text):
        button = Button(text=input_text, command=self.clicked).pack()


if __name__ == "__main__":
    app = GUI()
    app.status()
    app.createbutton("Hello World")
    app.mainloop()