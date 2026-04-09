from storage import load_tasks, save_tasks

def generate_task_id(tasks):
    if not tasks:
        return 1
    else:
        ids = [task["id"] for task in tasks]
        return max(ids) + 1

def add_task(description, timestamp):
    tasks = load_tasks()
    new_task = {
        "id": generate_task_id(tasks),
        "description": description,
        "status": "to-do",
        "created": timestamp,
        "updated": timestamp
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task added successfully! (ID: {new_task['id']})")

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
    tasks = load_tasks()
    found = False

    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            found = True
            break
    
    if found:
        save_tasks(tasks)
        print(f"Task {task_id} deleted successfully!")
    else:
        print(f"Task with ID {task_id} not found.")

def mark_in_progress(task_id):
    tasks = load_tasks()
    found = False
    
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "in-progress"
            save_tasks(tasks)
            print(f"Task {task_id} marked as in progress!")
            found = True
            break

    if not found:
        print(f"Task with ID {task_id} not found.")

def mark_done(task_id):
    tasks = load_tasks()
    found = False

    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "done"
            save_tasks(tasks)
            print(f"Task {task_id} marked as done!")
            found = True
            break

    if not found:
        print(f"Task with ID {task_id} not found.")

def list_tasks(status=None):
    tasks = load_tasks()
    valid_status = ["to-do", "in-progress", "done"]

    if status is not None and status not in valid_status:
        print("Unknown status. Valid options are: to-do, in-progress, done.")
        return

    if status:
        print(f"Listing tasks with status: {status}")
    else:
        print("Listing all tasks")

    filtered_tasks = []

    for task in tasks:
        if status is None or task["status"] == status:
            filtered_tasks.append(task)

    if not filtered_tasks:
        print("No tasks found.")
        return

    for task in filtered_tasks:
        print(
            f"ID: {task['id']} | "
            f"Description: {task['description']} | "
            f"Status: {task['status']} | "
            f"Created: {task['created']} | "
            f"Updated: {task['updated']}"
        )