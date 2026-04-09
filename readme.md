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

  * `todo`
  * `in-progress`
  * `done`

---

## Task Properties

Each task stored in the system contains the following properties:

| Property        | Description                                    |
| --------------- | ---------------------------------------------- |
| **id**          | Unique identifier for each task                |
| **description** | Short description of the task                  |
| **status**      | Current status (`todo`, `in-progress`, `done`) |
| **createdAt**   | Timestamp when the task was created            |
| **updatedAt**   | Timestamp when the task was last modified      |

Tasks are stored in a **JSON file** in the current directory.

---

## Project Requirements

This project follows the following constraints:

* Runs entirely from the **command line**
* Uses **positional arguments** for commands
* Stores tasks in a **JSON file**
* Automatically creates the JSON file if it does not exist
* Uses only **native language modules**
* No external libraries or frameworks

---

## CLI Usage

### Add a Task

```bash
task-cli add <Task Description>
```

Output:

```bash
Task added successfully (ID: <id>)
```

---

### Update a Task

```bash
task-cli update <id> <New Task Description>
```

---

### Delete a Task

```bash
task-cli delete <id>
```

---

### Mark Task Status

Mark a task as **in progress**:

```bash
task-cli mark-in-progress <id>
```

Mark a task as **done**:

```bash
task-cli mark-done <id>
```

---

### List Tasks

List all tasks:

```bash
task-cli list
```

List tasks by status:

```bash
task-cli list done
task-cli list todo
task-cli list in-progress
```

---

## Storage

All tasks are stored in a local JSON file:

```
tasks.json
```

The file is automatically created when the first task is added.

---

## Project Structure

```
task-cli/
│
├── main.py
├── task_manager.py
├── storage.py
├── tasks.json
└── README.md
```

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/HarshNaidu/Task-Tracker-CLI.git
cd task-cli
```

### 2. Run the CLI

```bash
python main.py
task-cli help 
```

---

## Purpose of the Project

This project is designed as a **practice exercise** to strengthen programming fundamentals including:

* CLI application development
* Data persistence using JSON
* Handling user input
* Writing modular and maintainable code

---

## Future Improvements

Possible extensions include:

* Task priorities
* Due dates
* SQLite database storage
* Colored CLI output
* Packaging as an installable Python CLI tool

---

## License

This project is open-source and available under the **MIT License**.
