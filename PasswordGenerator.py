from tkinter import *
from tkinter.messagebox import *
from tkinter import messagebox
import random


font_style_heading = ("arial", 30, "bold", "underline")
font_buttons = ("arial", 12, "bold")
font_style_label = ("arial", 12)
color = "blue"


# creating class of password generator app
class PasswordGenerator:
    def __init__(self):
        self.guiWindow = Tk()
        self.guiWindow.title("Password Generator")
        self.guiWindow.geometry("500x500")
        self.guiWindow.resizable(0, 0)
        # creating label and their entry field
        self.heading_label = Label(self.guiWindow, text="Password Generator",
                                   font=font_style_heading, foreground=color)
        self.heading_label.pack()

        # username textfield and label
        self.user_label = Label(self.guiWindow, text="Enter user name:",
                                justify=LEFT, font=font_style_label)
        self.user_label.place(x=70, y=85)
        self.user_text = Entry(self.guiWindow, justify="center",
                               font=font_style_label)
        self.user_text.place(x=250, y=85)

        # password length textfield and label
        self.label_length = Label(self.guiWindow, text="Password Length:",
                                  justify="left", font=font_style_label)
        self.label_length.place(x=70, y=145)
        self.length_text = Entry(self.guiWindow, justify="center",
                                 font=font_style_label)
        self.length_text.place(x=250, y=145)

        # generate password textfield and label
        self.password_generate_label = Label(self.guiWindow, text="Generate Password:",
                                             justify="left", font=font_style_label)
        self.password_generate_label.place(x=70, y=195)
        self.password_generate_text = Entry(
            self.guiWindow, justify="center", font=font_style_label)
        self.password_generate_text.place(x=250, y=195)

        # creating Button
        self.generate_password_button = Button(
            self.guiWindow, text="GENERATE PASSWORD", justify="center", bg=color, height=2, width=22, font=font_buttons, relief=SOLID, foreground="white", command=self.generate_password)
        self.generate_password_button.place(x=160, y=250)

        self.accept_button = Button(self.guiWindow, text="ACCEPT", justify="center", bg="green",
                                    height=2, width=12, font=font_buttons, foreground="white", relief=SOLID, command=self.accept_password)
        self.accept_button.place(x=210, y=320)

        self.reset_button = Button(self.guiWindow, text="RESET", justify="center", height=2, bg="grey",
                                   width=12, font=font_buttons, foreground="white", relief=SOLID, command=self.reset_password)
        self.reset_button.place(x=210, y=400)

        self.guiWindow.mainloop()

    # creating functionality for buttons
    def generate_password(self):
        try:
            user_name = self.user_text.get()
            if not user_name:
                messagebox.showerror(
                    "ERROR", "Field is empty please enter your username")
                return

            # initializing max length to generate password
            max_length = int(self.length_text.get())
            if max_length < 8:
                messagebox.showerror(
                    "ERRO", " length of password should be at least  character")
                return

            # generating password from giving length
            character = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()"

            password = " "

            for _ in range(max_length):
                password += ''.join(random.choice(character))

            self.password_generate_text.delete(0, END)
            self.password_generate_text.insert(0, password)
        except:
            messagebox.showerror("ERROR", "Length of password is required")
            return

    def accept_password(self):
        password = self.password_generate_text.get()
        if password:
            messagebox.showinfo("Accepted", "your password is accepted")
        else:
            messagebox.showerror("ERROR", "There are no password to generate")
            return

    def reset_password(self):
        self.length_text.delete(0, END)
        self.password_generate_text.delete(0, END)


if __name__ == "__main__":
    pass_generate = PasswordGenerator()
