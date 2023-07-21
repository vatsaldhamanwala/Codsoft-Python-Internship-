from tkinter import *
from tkinter import messagebox
import math

font_style = ("arial", 20, "bold")


# creating functionality to perform operation
def clear_all():
    text_input.delete(0, END)


def clear_one_by_item():
    expression = text_input.get()
    expression = expression[0:len(expression)-1]
    text_input.delete(0, END)
    text_input.insert(0, expression)


def click_on_button(event):
    button = event.widget
    text = button['text']

    # performing arithmetic operation using eval() method

    if text == "√":
        try:
            expression = text_input.get()
            result = math.sqrt(float(expression))
            text_input.delete(0, END)
            text_input.insert(0, result)
        except:
            text_input.delete(0, END)
            text_input.insert(END, "ERROR")

    if text == "=":
        try:
            expression = text_input.get()
            result = eval(expression)
            text_input.delete(0, END)
            text_input.insert(0, result)
        except Exception:
            text_input.delete(0, END)
            text_input.insert(END, "ERROR")
        return

    text_input.insert(END, text)


# creating window for calculator app
guiWindow = Tk()
guiWindow.title("Calculator")
guiWindow.geometry("400x400")
guiWindow.resizable(0, 0)


# creating text field
text_input = Entry(guiWindow, font=font_style, justify="right")
text_input.pack(side=TOP, pady=10, fill=X, padx=10)

# Creating button and frames
button_frame = Frame(guiWindow)
button_frame.pack(side=TOP, padx=10)

# Looping buttons digits usins for loop
output = 1
for i in range(1, 4):
    for j in range(0, 3):
        buttons = Button(button_frame, text=str(
            output), font=font_style, width=5, relief="ridge", activebackground="powder blue")
        buttons.grid(row=i, column=j)
        output += 1
        buttons.bind('<Button-1>', click_on_button)


# Other buttons functionality
button_all_clear = Button(button_frame, text="AC",
                          font=font_style, width=5, relief="ridge", activebackground="powder blue", command=clear_all)
button_all_clear.grid(row=0, column=0)

button_clear = Button(button_frame, text="C",
                      font=font_style, width=5, relief="ridge", activebackground="powder blue", command=clear_one_by_item)
button_clear.grid(row=0, column=1)

button_square_root = Button(button_frame, text="√",
                            font=font_style, width=5, relief="ridge", activebackground="powder blue", command=clear_one_by_item)
button_square_root.grid(row=0, column=2)


button_0 = Button(button_frame, text="0",
                  font=font_style, width=11, relief="ridge", activebackground="powder blue")
button_0.grid(row=4, column=0, columnspan=2)

button_dot = Button(button_frame, text=".",
                    font=font_style, width=5, relief="ridge", activebackground="powder blue")
button_dot.grid(row=4, column=2)

button_equal = Button(button_frame, text="=",
                      font=font_style, width=5, relief="ridge", activebackground="powder blue")
button_equal.grid(row=4, column=3)

button_plus = Button(button_frame, text="+",
                     font=font_style, width=5, relief="ridge", activebackground="powder blue")
button_plus.grid(row=0, column=3)

button_minus = Button(button_frame, text="-",
                      font=font_style, width=5, relief="ridge", activebackground="powder blue")
button_minus.grid(row=1, column=3)

button_multiply = Button(button_frame, text="*",
                         font=font_style, width=5, relief="ridge", activebackground="powder blue")
button_multiply.grid(row=2, column=3)

button_division = Button(button_frame, text="/",
                         font=font_style, width=5, relief="ridge", activebackground="powder blue")
button_division.grid(row=3, column=3)

# Bind all other button to perform task
button_0.bind('<Button-1>', click_on_button)
button_dot.bind('<Button-1>', click_on_button)
button_equal.bind('<Button-1>', click_on_button)
button_plus.bind('<Button-1>', click_on_button)
button_minus.bind('<Button-1>', click_on_button)
button_multiply.bind('<Button-1>', click_on_button)
button_division.bind('<Button-1>', click_on_button)
button_square_root.bind('<Button-1>', click_on_button)

guiWindow.mainloop()
