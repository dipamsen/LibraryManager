import tkinter as tk
import tkinter.font as tkFont

screens = []


def goto(screen):
    for i in screens:
        i.pack_forget()
    screen.pack()


app = tk.Tk()
font = tkFont.Font(family="Helvetica", size=12, weight="normal")
app.title("Library Management System")
app.geometry("500x500")
app.configure(bg="light blue")
app.option_add("*Font", font)

homescrn = tk.Frame(app)
homescrn.config(background="SystemWindow")
# homescrn.attributes("-transparent", True)
screens.append(homescrn)
homescrn.pack()


label = tk.Label(homescrn, text="Library Management System", font=("Arial", 20))
label.pack(pady=10)

app.mainloop()
