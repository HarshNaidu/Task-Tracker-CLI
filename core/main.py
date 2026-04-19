from datetime import datetime

from cli.task_manager import (
                            add_task, 
                            delete_task, 
                            list_tasks, 
                            mark_done, 
                            mark_in_progress, 
                            update_task
                        )


def main():
    print("Task Tracker CLI (type 'help' for commands, 'exit' to quit)")

    while True:
        cmd = input(">> ").strip()

        if not cmd:
            continue

        args = cmd.split()
        command = args[0]

        if command == "exit":
            break

        elif command == "help":
            print("Available commands:")
            print("add <task description>")
            print("update <task id> <new description>")
            print("delete <task id>")
            print("mark-in-progress <task id>")
            print("mark-done <task id>")
            print("list")
            print("list <status>")

        elif command == "add":
            task_description = " ".join(args[1:]).strip().strip('"').strip("'")
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            if not task_description:
                print("Task description cannot be empty.")
            else:
                add_task(task_description, timestamp)

        elif command == "update":
            task_id = int(args[1])
            new_description = " ".join(args[2:]).strip().strip('"').strip("'")
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            if not new_description:
                print("Task description cannot be empty.")
            else:
                update_task(task_id, new_description, timestamp)

        elif command == "delete":
            task_id = int(args[1])
            delete_task(task_id)

        elif command == "mark-in-progress":
            task_id = int(args[1])
            mark_in_progress(task_id)

        elif command == "mark-done":
            task_id = int(args[1])
            mark_done(task_id)

        elif command == "list":
            if len(args) == 1:
                list_tasks()
            else:
                list_tasks(args[1])

        else:
            print("Unknown command. Type 'help'.")