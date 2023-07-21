import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


# addind task into to-do lists


def add_task():
    task_name = task_field.get()
    if task_name:
        task_listbox.insert("end", task_name)
        task_field.delete(0, "end")
    else:
        messagebox.showerror("ERROR", "Fields are empty")


def update_task():
    try:
        task_update = task_listbox.curselection()

        task = task_listbox.get(task_update)
        task_field.insert("end", task)
        task_listbox.delete(task_update)
    except Exception as e:
        print("selet task to edit", e)
        messagebox.showerror("ERROR", "Please select a task to edit.", e)


def delete_task():
    try:
        delete_item = task_listbox.curselection()
        task_listbox.delete(delete_item)
    except:
        messagebox.showerror("ERROR", "Task Not Selected.Cannnot Delete")


def clear_list():
    task_listbox.delete(0, "end")


# Main Functionality of To Do List Application starts here...!
if __name__ == '__main__':

    # creating main window for to-do list app
    guiWindow = tk.Tk()
    guiWindow.title("TO-DO List App")
    guiWindow.geometry("500x450")
    guiWindow.resizable(0, 0)
    guiWindow.configure(bg="blue")

    # creating frame using tk.Frames()
    header_frame = tk.Frame(guiWindow, bg="#FAEBD7")
    functions_frames = tk.Frame(guiWindow, bg="#FAEBD7")
    listbox_frame = tk.Frame(guiWindow, bg="#FAEBD7")

    # using pack() method to place the frames in the app
    header_frame.pack(fill="both")
    functions_frames.pack(side="left", expand=True, fill="both")
    listbox_frame.pack(side="right", expand=True, fill="both")

    # creating labels using ttk.Label()
    header_label = ttk.Label(
        header_frame,
        text="To-Do List",
        font=("Arel", "30"),
        background="#FAEBD7",
        foreground="#8B4513"
    )
    header_label.pack(padx=20, pady=20)

    task_label = ttk.Label(
        functions_frames,
        text="Add Items",
        font=("Consolas", "11", "bold"),
        background="#FAEBD7",
        foreground="black"
    )

    task_label.pack(padx=30, pady=40)

    # create entry field using Entry()
    task_field = ttk.Entry(
        functions_frames,
        font=("Consolas", "12"),
        width=18,
        background="white",
        foreground="blue"
    )

    task_field.place(x=30, y=80)

    # creating Buttons using ttk.Button()
    add_button = ttk.Button(
        functions_frames,
        text="Add",
        width=24,
        command=add_task
    )

    edit_button = ttk.Button(
        functions_frames,
        text="Edit",
        width=24,
        command=update_task
    )
    del_button = ttk.Button(
        functions_frames,
        text="Delete",
        width=24,
        command=delete_task
    )

    # using place() method to set position of buttons
    add_button.place(x=30, y=120)
    del_button.place(x=30, y=160)
    edit_button.place(x=30, y=200)

    # defining list box using tk.Listbox()
    task_listbox = tk.Listbox(
        listbox_frame,
        width=26,
        height=13,
        selectmode="SINGLE",
        background="#FFFFFF",
        foreground="black",
        selectbackground="#CD853F",
        selectforeground="#FFFFFF"
    )

    task_listbox.place(x=10, y=20)
    guiWindow.mainloop()
