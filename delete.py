#Handles deleting tasks by list index.

from task_list import tasks
from show import show_tasks

def delete_task():
    show_tasks()
    if len(tasks) == 0:
        return

    task_num = input("Enter the task number to delete: ")
    if task_num.isdigit():
        index = int(task_num) - 1
        if 0 <= index < len(tasks):
            removed_task = tasks.pop(index)
            print(f"Removed task: {removed_task}")
        else:
            print("Invalid task number.")
    else:
        print("Please enter a valid number.")
