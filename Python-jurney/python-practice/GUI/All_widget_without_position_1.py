import tkinter as tk
from tkinter import messagebox, scrolledtext
from tkinter.ttk import Combobox

# Initialize main window
window = tk.Tk()
window.title("Improved GUI")
window.geometry("400x500")  # Set window size

# Function to handle "Enter" button click
def clicked():
    name = txt.get()
    bt.configure(text=f"Welcome {name}")

# Function to show message box with selected values
def show_message():
    name = txt.get()
    radio_choice = selected_option.get()
    radio_text = radio_map.get(radio_choice, "None")
    message = f"Hello {name}!\nSelected Topic: {radio_text}"
    messagebox.showinfo("Information", message)

# --- Widgets ---

# Label
label = tk.Label(window, text="Hello Mayur!", bg="red", fg="yellow", font=("Arial", 14))
label.pack(pady=10)

# Entry
txt = tk.Entry(window, width=30)
txt.pack(pady=5)

# Button
bt = tk.Button(window, text="Enter", bg="pink", fg="black", command=clicked)
bt.pack(pady=5)

# Combobox
combo_label = tk.Label(window, text="Select a value:")
combo_label.pack()
combo = Combobox(window)
combo['values'] = (1, 2, 3, 45, "text data")
combo.current(1)
combo.pack(pady=5)

# Checkbutton
chk_state = tk.BooleanVar(value=True)
chk = tk.Checkbutton(window, text='Check me!', variable=chk_state)
chk.pack(pady=5)

# Radio buttons
radio_frame = tk.Frame(window)
radio_frame.pack(pady=10)

tk.Label(radio_frame, text="Choose a topic:").pack()

selected_option = tk.IntVar(value=0)
radio_map = {
    1: "Python",
    2: "DevOps",
    3: "Scaler"
}
tk.Radiobutton(radio_frame, text='Python', variable=selected_option, value=1).pack(anchor='w')
tk.Radiobutton(radio_frame, text='DevOps', variable=selected_option, value=2).pack(anchor='w')
tk.Radiobutton(radio_frame, text='Scaler', variable=selected_option, value=3).pack(anchor='w')

# ScrolledText
tk.Label(window, text="Enter your notes:").pack()
TXT = scrolledtext.ScrolledText(window, width=40, height=5)
TXT.pack(pady=5)

# Message Box Button
msg_btn = tk.Button(window, text="Show Message", command=show_message)
msg_btn.pack(pady=20)

# Create a Spinbox
spin = tk.Spinbox(window, from_=0, to=100, width=5)
spin.pack(pady=20)

# Start GUI loop
window.mainloop()
