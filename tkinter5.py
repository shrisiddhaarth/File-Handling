from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk # => pip install pillow

root = Tk()
root.title("Tkinter Basics")
root.geometry("400x400")

def show_image():
    img_window = Toplevel(root)
    img_window.title("Image Window")

    img = Image.open("Nemo.jpeg")
    img = img.resize((200, 200))
    img_tk = Image.Tk.PhotoImage(img)

    img_label = Label(img_window, image=img_tk)
    img_label.image = img_tk
    img_label.pack()

def show_message():
    messagebox.showinfo("Your msg", "Hello Friend!")

def open_top_window():
    top = Toplevel(root)
    top.title("Top Window")
    top.geometry("250x150")
    Label(top, text="New Top Window!", font=("Arial", 12)).pack(pady=20)

btn1 = Button(root, text="Show Image", command=show_image)
btn1.pack(pady=10)

btn2 = Button(root, text="Show Message Box", command=show_message)
btn2.pack(pady=10)

btn3 = Button(root, text="Open Top Window", command=open_top_window)
btn3.pack(pady=10)

root.mainloop()