from tkinter import *
from tkinter import font
from PIL import Image, ImageTk



root = Tk()
root.configure(width=800, height=600)

rem = font.Font(family="Bahnschrift", size=32, weight="bold")

logo = Image.open("librart.png")
logo = logo.resize((80, 80))
logo = ImageTk.PhotoImage(logo)
img = Label(root, image=logo)
img.pack()

title = Label(root, text="Library Manager")
title.config(font=rem)
title.pack()


root.mainloop()