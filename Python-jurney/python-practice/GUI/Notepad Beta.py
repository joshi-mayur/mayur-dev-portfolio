#creating Notepad
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os
def newFile():
    global file
    root.title("Untitled - Notepad")
    file=None
    TextArea.delete(1.0, END)

def openFile():
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*")])
    if file=="":
        file = None
    else:
        root.title(os.path.basename(file)+ " - Notepad")
        TextArea.delete(1.0, END)
        f=open(file,"r")
        TextArea.insert(1.0, f.read())
        f.close()

def saveFile():
    global file
    if file==None:
        file=asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt")
        if file=="":
            file = None
        else:
            #save as new file
            f = open(file,"w")
            f.write(TextArea.get(1.0, END))
            f.close()
            root.title(os.path.basename(file)+ " - Notepad")

def quitApp():
    root.destroy()

def cut():
    TextArea.event_generate("<<Cut>>")

def copy():
    TextArea.event_generate("<<Copy>>")

def paste():
    TextArea.event_generate("<<Paste>>")

def About():
    showinfo(title="Notepad", message="Notepad Version 1.0 ")


if __name__ == '__main__':
    root=Tk()
    root.geometry("644x788")
    root.title("untitled-Notepad")
    root.wm_iconbitmap("notepad.ico")

    #Add Text area
    TextArea = Text(root,font="lucida 13")
    file = None
    TextArea.pack(fill=BOTH, expand=1) #expand means take parent width

    #creating menubar
    MenuBar = Menu(root)
    FileMenu = Menu(MenuBar, tearoff=False)

    #to open new file
    FileMenu.add_command(label="New", command=newFile)

    #open existing file
    FileMenu.add_command(label="Open", command=openFile)

    #save the file
    FileMenu.add_command(label="Save",command=saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label="Exit",command=quitApp)

    MenuBar.add_cascade(label="File", menu=FileMenu)

    #Edit menu
    EditMenu=Menu(MenuBar, tearoff=False)
    EditMenu.add_command(label="cut",command=cut)
    EditMenu.add_command(label="copy",command=copy)
    EditMenu.add_command(label="paste",command=paste)

    MenuBar.add_cascade(label="Edit", menu=EditMenu)

    #help Menu
    HelpMenu = Menu(MenuBar, tearoff=False)
    HelpMenu.add_command(label="About Notepad",command=About)
    MenuBar.add_cascade(label="Help", menu=HelpMenu)


    root.config(menu=MenuBar)

    #adding scroll bar
    scroll = Scrollbar(TextArea)
    scroll.pack(side=RIGHT, fill=Y)
    scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=scroll.set)








    root.mainloop()