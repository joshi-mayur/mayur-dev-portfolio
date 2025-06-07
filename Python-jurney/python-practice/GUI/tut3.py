from tkinter import *
root = Tk()
root.geometry("800x233")
root.title("My GUI with joshi")

#import label options
# text - add the text
# bg=bakground
# fg - foreground
# font - sets the font
#       1. font=("comicsansms",10,"bold")
#       2. font="comicsansms 10 bold"
# padx - x padding
# pady - y padding
# relief - border styling - SUNKEN ,RAISED, GROOVE , RIDGE

TITLE_label= Label(text=''' Allu Arjun (born 8 April 1982) is an Indian actor who works in Telugu cinema.\n
He is one of the highest-paid actors in Indian cinema and has been featured in Forbes India's Celebrity 100 list since 2014.
\nAllu Arjun's accolades include a National Film Award,\n six Filmfare Awards, and three Nandi Awards.''',
                   bg="black" , fg ="white" , padx=23 , pady=94 ,font=("comicsansms",10,"bold"),borderwidth=3 , relief=RAISED)

# important pack
# anchor = nw
# side = top , bottom , left , right
# fill
# padx
# pady
TITLE_label.pack(side=LEFT, fill=Y)





TITLE_label.pack()
root.mainloop()




root.mainloop()