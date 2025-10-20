# main app
from tkinter import *
root = Tk()
root.title("Tkinter basics")
root.geometry("300x200")

def data():
    print("Data submitted")

# Creating widgets
label = Label(root, text="Welcomme to Tkinter!" , font=("Arial", 12))
entry = Entry(root, width=20)
button = Button(root, text="Submit", command=data)

# Using grid layout to arrange widgets
label.grid(row=0, column=0, columnspan=2, pady=5) # Label at row 0
entry.grid(row=1, column=0, columnspan=5, pady=5) # Entry at row 1, column 0
button.grid(row=1, column=1, columnspan=5, pady=5) # Button at row 1, column 1

# Running the application
root.mainloop()