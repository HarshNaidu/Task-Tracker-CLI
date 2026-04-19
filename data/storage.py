import json

file_name = "tasks.json"

def load_tasks():
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    

def save_tasks(tasks):
    with open(file_name, "w") as file:
        json.dump(tasks, file, indent=4)

