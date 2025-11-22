#Main menu loop and user interaction.

from show import show_tasks
from add import add_task
from delete import delete_task

while True:
    print("\nMenu:")
    print("1. Show tasks")
    print("2. Add a task")
    print("3. Delete a task")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == '1':
        show_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        delete_task()
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Please choose a number from 1 to 4.")
