#Contains logic for adding new tasks.

from task_list import tasks

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added!")
