# add, delete, list, quit

instructions = """
Usage:
- Press a to add a task
- Press d to delete a task
- Press l to list all tasks
- Press q to quit"""

print(instructions)

todo = []

while True:
    cmd = input("Enter a command: ")
    if cmd == "a":
        task = input("Enter a task: ")
        todo.append(task)
        print("Task added: ", task)
    elif cmd == "d":
        if todo:
            print("Tasks: ")
            for i in todo:
                print(i)
            task = input("Enter a task to delete: ")
            if task in todo:
                todo.remove(task)
                print("Task deleted:", task)
            else:
                print("Task not found!")
        else:
            print("No tasks to delete!")
    elif cmd == "l":
        if todo:
            print("Tasks: ")
            for i in todo:
                print(i)
        else:
            print("No tasks to list!")
    elif cmd == "q":
        break
    else:
        print("Invalid command")


# python3 main.py 
# Usage:
# - Press a to add a task
