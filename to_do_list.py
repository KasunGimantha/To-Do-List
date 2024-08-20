import tkinter as tk
from tkinter import Label, font

root = tk.Tk()
root.config(bg="light blue")

root.title("To-Do List")
root.geometry("400x400")
# styling section
font_style = font.Font(family="Ariel", size=13)
title_style = font.Font(family="Arial", size=15, weight="bold")
# label section
title_label = tk.Label(root, text="To Do List",
                       bg="light blue", font=title_style)
completed_label = tk.Label(root, text="Completed Tasks",
                           bg="light blue", font=font_style)
entry_widget = tk.Entry(root, bg="light yellow")
task_name = entry_widget.get()
pending_label = tk.Label(root, text="Pending Tasks",
                         bg="light blue", font=font_style)
# listbox
todo_listbox = tk.Listbox(root, selectmode=tk.SINGLE, bg="light yellow")
completed_listbox = tk.Listbox(root, bg="light yellow")

# method section


def clear_list():
    completed_listbox.delete(0, tk.END)


def switch_task():
    selected_indices = todo_listbox.curselection()
    for idx in reversed(selected_indices):
        item = todo_listbox.get(idx)
        completed_listbox.insert(tk.END, item)
        todo_listbox.delete(idx)


def task_delete():
    selected_indices = todo_listbox.curselection()
    for idx in reversed(selected_indices):
        todo_listbox.delete(idx)


def update_listbox():
    task_name = entry_widget.get()
    todo_listbox.insert(tk.END, task_name)
    entry_widget.delete(0, tk.END)

    # button section
add_button = tk.Button(root, text="Add Task",
                       command=update_listbox, bg="yellow")
remove_button = tk.Button(root, text="Remove Task",
                          command=task_delete, bg="yellow")
switch_button = tk.Button(root, text="Mark as Complete",
                          command=switch_task, bg="yellow")
clear_button = tk.Button(
    root, text="Clear Completed Tasks", command=clear_list, bg="yellow")
title_label.place(x=145, y=10)
completed_label.place(x=250, y=110)
add_button.place(x=5, y=50)
entry_widget.place(x=80, y=50)
remove_button.place(x=5, y=80)
pending_label.place(x=5, y=110)
todo_listbox.place(x=5, y=140)
switch_button.place(x=5, y=320)
completed_listbox.place(x=250, y=140)
clear_button.place(x=250, y=320)
root.mainloop()
