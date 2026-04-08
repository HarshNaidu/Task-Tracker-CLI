import json

fileName = "tasks.json"

def load_tasks():
    try:
        with open(fileName, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def save_tasks(tasks):
    with open(fileName, "w") as file:
        json.dump(tasks, file, indent=4)

