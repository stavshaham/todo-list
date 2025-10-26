# main.py - by Stav Shaham
# This file is the main file of the to do list project. It includes the GUI mostly, and calls functions from different modules

import tkinter as tk
import tkinter.ttk as ttk
import tasks as ts
from tkinter import messagebox
import file_handler as fh

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
    ts.tasks = [task for task in ts.tasks if not task["done"]]
    fh.save_data(ts.tasks)
    update_tasks()

# This function updates the list box (the view)
def update_tasks():
    """
    This function updates the tasks list
    :return:
    """
    # Clear old checkboxes
    for widget in root.checkbox_frame.winfo_children():
        widget.destroy()

    for i, task in enumerate(ts.tasks):
        var = tk.BooleanVar(value=task["done"])

        def on_toggle(index, v, widget):
            ts.tasks[index]["done"] = v.get()
            fh.save_data(ts.tasks)
            style_checkbox(widget, v.get())

        chk = tk.Checkbutton(
            root.checkbox_frame,
            text=task["name"],
            variable=var,
            bg="#1e1e1e",
            selectcolor="#1e1e1e",
            activebackground="#1e1e1e",
            anchor="w"
        )

        chk.pack(anchor="w", pady=3)
        style_checkbox(chk, task["done"])
        chk.config(command=lambda index=i, v=var, widget=chk: on_toggle(index, v, widget))

# Make the canvas scroll to fit content
def on_frame_config(event):
    """
    This function is called when the frame is configured
    :param event:
    :return:
    """
    canvas.configure(scrollregion=canvas.bbox("all"))

# This function is the design of the checkbox
def style_checkbox(chk, done):
    """
    This function checks if the task is done
    :param chk:
    :param done:
    :return:
    """
    if done:
        chk.config(fg="gray", font=("Arial", 12, "overstrike"))
    else:
        chk.config(fg="white", font=("Arial", 12, "normal"))

# This function allows mouse wheel
def _on_mousewheel(event):
    """
    This function is called when the mouse wheel changes
    :param event:
    :return:
    """
    # macOS delta is small (±1), Windows is larger (±120)
    delta = event.delta
    if delta == 0:
        return

    # Normalize scroll speed
    if delta > 0:
        canvas.yview_scroll(-1, "units")
    else:
        canvas.yview_scroll(1, "units")

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
canvas = tk.Canvas(root.main_frame, bg="#1e1e1e", highlightthickness=0)
scrollbar = ttk.Scrollbar(root.main_frame, orient="vertical", command=canvas.yview)
root.checkbox_frame = tk.Frame(canvas, bg="#1e1e1e")

# Place checkbox frame inside canvas
canvas.create_window((0, 0), window=root.checkbox_frame, anchor="nw")

root.checkbox_frame.bind("<Configure>", on_frame_config)
canvas.configure(yscrollcommand=scrollbar.set)

# Layout
canvas.grid(row=1, column=0, sticky="nsew")
scrollbar.grid(row=1, column=1, sticky="ns")

canvas.bind("<Enter>", lambda e: canvas.bind_all("<MouseWheel>", _on_mousewheel))
canvas.bind("<Leave>", lambda e: canvas.unbind_all("<MouseWheel>"))
root.checkbox_frame.bind("<Enter>", lambda e: canvas.bind_all("<MouseWheel>", _on_mousewheel))
root.checkbox_frame.bind("<Leave>", lambda e: canvas.unbind_all("<MouseWheel>"))

# Expand available space properly
root.main_frame.grid_rowconfigure(1, weight=1)
root.main_frame.grid_columnconfigure(0, weight=1)

# 4. Remove Task Button
root.remove_button = tk.Button(root.main_frame, text="Remove Done Tasks", command=remove_task)
root.remove_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

ts.load_data_from_file()
update_tasks()

root.mainloop()