# main.py - by Stav Shaham
# This file is the main file of the to do list project. It includes the GUI mostly, and calls functions from different modules

import tkinter as tk
import tasks as ts
from tkinter import messagebox

# This function adds a task to the list view
def add_task():
    """
    This function adds a task to the tasks list
    :return: None
    """
    task_name = root.task_entry.get().strip()
    if task_name:
        ts.add_task(task_name)
        update_tasks()
        root.task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You have to enter a task name")

# This function removes a task from the list
def remove_task():
    """
    This function removes a task from the tasks list
    :return:
    """
    try:
        index = root.task_listbox.curselection()[0]
        root.task_listbox.delete(index)
        update_tasks()
        ts.remove_task(index=index)
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to remove")

    update_tasks()

# This function updates the list box (the view)
def update_tasks():
    """
    This function updates the tasks list
    :return:
    """
    root.task_listbox.delete(0, tk.END)
    for task in ts.tasks:
        root.task_listbox.insert(tk.END, task)

root = tk.Tk()
root.geometry("500x500")
root.title("Todo List")

# Setting up main frame
root.main_frame = tk.Frame(root, padx=10, pady=10)
root.main_frame.pack()

# --- GUI Widgets will go here ---

# 1. Task Entry Field
root.task_entry = tk.Entry(root.main_frame, width=40)
root.task_entry.grid(row=0, column=0, padx=5, pady=5)

# 2. Add Task Button
root.add_button = tk.Button(root.main_frame, text="Add Task", command=add_task)
root.add_button.grid(row=0, column=1, padx=5, pady=5)

# 3. Task List Box
root.task_listbox = tk.Listbox(root.main_frame, width=50, height=15)
root.task_listbox.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

# 4. Remove Task Button
root.remove_button = tk.Button(root.main_frame, text="Remove Selected", command=remove_task)
root.remove_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

ts.load_data_from_file()
update_tasks()

root.mainloop()