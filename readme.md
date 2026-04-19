# Task Tracker CLI

A simple **Command Line Interface (CLI)** application to manage and track tasks.
The tool allows users to add, update, delete, and monitor tasks directly from the terminal.

This project demonstrates core programming concepts such as:

* Command-line argument handling
* File system operations
* JSON-based data storage
* Error handling
* Modular program design

---

## Features

* Add new tasks
* Update existing tasks
* Delete tasks
* Mark tasks as **in-progress** or **done**
* List all tasks
* Filter tasks by status:

  * `to-do`
  * `in-progress`
  * `done`

---

## Task Properties

Each task stored in the system contains the following properties:

| Property        | Description                                     |
| --------------- | ----------------------------------------------- |
| **id**          | Unique identifier for each task                 |
| **description** | Short description of the task                   |
| **status**      | Current status (`to-do`, `in-progress`, `done`) |
| **created**     | Timestamp when the task was created             |
| **updated**     | Timestamp when the task was last modified       |

Tasks are stored in a **JSON file** managed internally by the application.

---

## Project Requirements

This project follows the following constraints:

* Runs entirely from the **command line**
* Uses **positional arguments / interactive commands**
* Stores tasks in a **JSON file**
* Automatically creates the JSON file if it does not exist
* Uses only **native Python modules**
* No external libraries or frameworks

---

## CLI Usage

### Start the CLI

```bash
task-cli
```

---

### Available Commands

```bash
add <description>
update <id> <new-description>
delete <id>
mark-in-progress <id>
mark-done <id>
list
list <status>
exit
```

---

### Example

```bash
>> add Gym
>> list
>> mark-done 1
>> delete 1
>> exit
```

---

## Storage

All tasks are stored in a local JSON file (not tracked in version control):

```
data/tasks.json
```

The file is automatically created when the first task is added.

---

## Project Structure

```
Task-Tracker-CLI/
│
├── cli/
│   └── task_manager.py
├── core/
│   └── main.py
├── data/
│   └── storage.py
│
├── setup.py
├── README.md
```

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/HarshNaidu/Task-Tracker-CLI.git
cd Task-Tracker-CLI
```

---

### 2. Install the CLI

```bash
pip install -e .
```

---

### 3. Run the Application

```bash
task-cli
```

---

## Purpose of the Project

This project is based on the
[Task Tracker Project](https://roadmap.sh/projects/task-tracker)
and is intended to strengthen:

* CLI application development
* Data persistence using JSON
* Handling user input
* Writing modular, maintainable code

---

## Future Improvements

Possible extensions include:

* Task priorities
* Due dates
* SQLite database storage
* Colored CLI output
* Packaging and publishing as a pip-installable tool

---

## License

This project is open-source and available under the **MIT License**.
