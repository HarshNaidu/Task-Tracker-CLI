from storage import load_tasks, save_tasks

def add_task(description, timestamp):
    tasks = load_tasks()
    new_task = {
        "id": len(tasks) + 1,
        "description": description,
        "status": "to-do",
        "created": timestamp,
        "updated": timestamp
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task added successfully! (ID: {id})")

def update_task(task_id, new_description, timestamp):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_description
            task["updated"] = timestamp
            save_tasks(tasks)
        else:
            print(f"Task with ID {task_id} not found.")
            return
    print(f"Task {task_id} updated successfully!")

def delete_task(task_id):
    tasks= load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            save_tasks(tasks)
        else:
            print(f"Task with ID {task_id} not found.")
            return
    print(f"Task {task_id} deleted successfully!")

def mark_in_progress(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "in-progress"
            save_tasks(tasks)
        else:
            print(f"Task with ID {task_id} not found.")
            return
    print(f"Task {task_id} marked as in progress!")

def mark_done(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "done"
            save_tasks(tasks)
        else:
            print(f"Task with ID {task_id} not found.")
            return
    print(f"Task {task_id} marked as done!")

def list_tasks(status=None):
    if status == "todo" or status == "in-progress" or status == "done":
        print(f"Listing tasks with status: {status}")
    else:
        print("Listing all tasks")
    tasks = load_tasks()
    for task in tasks:
        if status is None or task["status"] == status:
            print(f"ID: {task['id']} | Description: {task['description']} | Status: {task['status']} | Created: {task['created']} | Updated: {task['updated']}")
        else:
            print(f"Unknown status: {status}. Valid options are: todo, in-progress, done.")


