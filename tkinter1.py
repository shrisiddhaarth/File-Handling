from tkinter import *

# basic window
root = Tk()
root.title("My First Tkinter Window") # Set title
root.geometry("400x300") # Set window size (width x height)
root.configure(bg="lightblue") # Change background color

entry = Entry(root)
entry.place(x= 100, y=100)
root.mainloop()
