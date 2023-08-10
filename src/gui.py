import tkinter as tk
import tkinter.font as tkFont


class ScreenManager:
    def __init__(self, root):
        self.root = root
        self.current_screen = None

    def show_screen(self, screen):
        if self.current_screen is not None:
            self.current_screen.pack_forget()  # Hide the current screen

        self.current_screen = screen
        self.current_screen.pack()  # Pack and show the new screen


def create_button_group(master, options):
    group = tk.Frame(master)
    group.pack(pady=10)
    for text, func in options:
        b = tk.Button(group, text=text, command=func)
        b.pack(anchor=tk.W)
    return group


def create_main_screen(master):
    screen = tk.Frame(master)
    # label = tk.Label(screen, text="Main Screen")
    # label.pack()
    options = [
        ("Admin", lambda: scm.show_screen(adminscrn)),
        ("User", lambda: scm.show_screen(userscrn)),
    ]
    create_button_group(screen, options)

    return screen


def create_admin_screen(master):
    screen = tk.Frame(master)
    label = tk.Label(screen, text="Other Screen")
    label.pack()
    return screen


app = tk.Tk()
font = tkFont.Font(family="Helvetica", size=12, weight="normal")
app.title("Library Management System")
app.geometry("500x500")
app.configure(bg="light blue")
app.option_add("*Font", font)

scm = ScreenManager(app)

homescrn = create_main_screen(app)
adminscrn = create_admin_screen(app)
# userscrn = tk.Frame(app)
label = tk.Label(app, text="Library Management System", font=("Arial", 20))
label.pack(pady=10)

scm.show_screen(homescrn)

app.mainloop()
