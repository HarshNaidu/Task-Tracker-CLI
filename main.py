from datetime import datetime
import sys
from task_manager import add_task, update_task, delete_task, mark_in_progress, mark_done, list_tasks
cmd = input("Welcome to Task Tracker! Please start with 'task-cli help' for a list of commands.\n")
sys.argv = cmd.split()

if sys.argv[0] != "task-cli":
    print(f"{cmd} is not a command. Please start with 'task-cli'.")
    sys.exit(1)

else:
    switcher = {
        "help": "help",
        "add": "add",
        "update": "update",
        "delete": "delete",
        "mark-in-progress": "mark-in-progress",
        "mark-done": "mark-done",
        "list": "list"
    }
    command = switcher.get(sys.argv[1], "Unknown command")
    if command == "Unknown command":
        print(f"Unknown command: {sys.argv[1]}. Please start with 'task-cli help' for a list of commands.")
        sys.exit(1)

    elif command == "help":
        print("Available commands:")
        print("  task-cli add <task description> - Add a new task")
        print("  task-cli update <task id> <new description> - Update a task's description")
        print("  task-cli delete <task id> - Delete a task")
        print("  task-cli mark-in-progress <task id> - Mark a task as in progress")
        print("  task-cli mark-done <task id> - Mark a task as done")
        print("  task-cli list - List all tasks")
        print("  task-cli list <status> - List tasks by status (todo, in-progress, done)")

    elif sys.argv[1] == "add":
        task_description = " ".join(sys.argv[2:])
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        add_task(task_description, timestamp)  

    elif sys.argv[1] == "update":
        task_id = int(sys.argv[2])
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_description = " ".join(sys.argv[3:])
        update_task(task_id, new_description, timestamp)  

    elif sys.argv[1] == "delete":
        task_id = int(sys.argv[2])
        delete_task(task_id)

    elif sys.argv[1] == "mark-in-progress":
        task_id = int(sys.argv[2])
        mark_in_progress(task_id)

    elif sys.argv[1] == "mark-done":
        task_id = int(sys.argv[2])
        mark_done(task_id)

    elif sys.argv[1] == "list":
            if len(sys.argv) == 2:
                list_tasks()
            else:
                list_tasks(sys.argv[2])
    else:
        print(f"Unknown command: {sys.argv[1]}. Please start with 'task-cli help' for a list of commands.")