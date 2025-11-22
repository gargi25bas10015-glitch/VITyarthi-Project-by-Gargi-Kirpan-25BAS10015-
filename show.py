#Responsible for displaying tasks from the list.

from task_list import tasks

def show_tasks():
    if len(tasks) == 0:
        print("Your to-do list is empty.")
    else:
        print("Your tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
