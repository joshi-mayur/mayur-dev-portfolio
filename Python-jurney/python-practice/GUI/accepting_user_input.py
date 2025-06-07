from tkinter import *
def get_values():
    print("Application submitted")
    with open("record.txt","a") as fp:
        fp.write(f"{name_value.get() ,mobile_value.get() , gender_value.get() , payment_value.get(),  foodservicevalue.get()} \n")


root = Tk()
root.geometry("600x444")
#Heading
Label(root, text="Welcome to joshi Travels", font="STHupo 13 bold").grid(row=0, column=3)

#Text for our form
name = Label(root, text="Name")
mobile_no = Label(root, text="Mobile")
gender = Label(root, text="Gender")
paymentmode = Label(root, text="Payment mode")

#pack text using grid
name.grid(row=1, column=2)
mobile_no.grid(row=2, column=2)
gender.grid(row=3, column=2)
paymentmode.grid(row=4, column=2)

#creating variable for storing entries
name_value = StringVar()
mobile_value = StringVar()
gender_value = StringVar()
payment_value = StringVar()
foodservicevalue = StringVar()

#Entry for our form
name_entry = Entry(root, textvariable=name_value)
mobile_entry = Entry(root, textvariable=mobile_value)
gender_entry = Entry(root, textvariable=gender_value)
payment_entry = Entry(root, textvariable=payment_value)

#ARRANGING entries
name_entry.grid(row=1, column=3)
mobile_entry.grid(row=2, column=3)
gender_entry.grid(row=3, column=3)
payment_entry.grid(row=4, column=3)

#checkbox
food_service = Checkbutton(text="Include Meal", variable=foodservicevalue)
food_service.grid(row=5, column=3)

#Button & packing it and assigning it a command
Button(text="Submit",command=get_values).grid(row=6,column=3)


root.mainloop()
