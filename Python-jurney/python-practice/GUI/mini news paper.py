#creating dummy news paper like text + image
from tkinter import *
from PIL import ImageTk, Image
root = Tk()
def every_100(text):
    final_txt=""
    for i in range(0,len(text)):
        final_txt+=text[i]
        if i%100==0 and i!=0:
            final_txt += "\n"
    return final_txt



root.title("Joshi ka Akhabaar")
root.geometry("1000x1000")

texts = []
photos = []
for i in range(0, 2):
    with open(f"{i + 1}.txt") as f:
        text = f.read()
        texts.append(every_100(text))

    image = Image.open(f"{i+1}.png")
    #resize the image
    image = image.resize((225,225), Image.Resampling.LANCZOS)
    photos.append(ImageTk.PhotoImage(image))


f0=Frame(root,width=900 , height=70)
Label(f0, text="code with joshi News",font= "Lucida 33 bold").pack()
Label(f0, text="May 11,2025", font="lucida 13 bold").pack()
f0.pack()


f1=Frame(root,width=900 , height=200)
Label(f1, text=texts[0],padx=22 , pady=22).pack(side="left")
Label(f1,image=photos[0],anchor="e").pack()
f1.pack(anchor="w")

f2=Frame(root,width=900 , height=200)
Label(f2, text=texts[1],padx=22 , pady=22).pack(side="left")
Label(f2,image=photos[1],anchor="e").pack()
f2.pack(anchor="w")


root.mainloop()