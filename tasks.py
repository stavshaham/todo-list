# tasks.py - by Stav Shaham
# This file is used to handle all tasks functions

import file_handler as fh
tasks = []

# This function adds a new task to the tasks
def add_task(task):
    """
    This function adds a task to the tasks dictionary.
    :argument task: The task to add.
    :type task: str
    :return: None
    """
    tasks.append(task)
    fh.save_data(tasks)

# This function removes a task from tasks
def remove_task(index):
    """
    This function removes a task from the tasks dictionary.
    :param index: The id of the task
    :type index: int
    :return: None
    """
    del tasks[index]
    fh.save_data(tasks)

# This function loads the data from the file every time we open the application
def load_data_from_file():
    """
    This function loads data from file.
    :return: None
    """
    data = fh.load_data()
    for task in data:
        add_task(task)

# This function returns all tasks as a dictionary
def view_tasks():
    """
    This function prints the tasks dictionary.
    :return tasks: the tasks list
    """
    return tasks