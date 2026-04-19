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

This project was developed to practice building a complete command-line tool from scratch, with an emphasis on structure, usability, and real-world execution.It focuses on:

* Structuring an application into clearly defined layers (CLI interface, core logic, and data handling)
* Designing an interactive command system for managing tasks efficiently
* Persisting application state using JSON-based storage
* Converting a Python script into a reusable, installable CLI tool
* Maintaining consistency in code organization and naming conventions
* Ensuring predictable behavior through basic validation and error handling

Beyond functionality, the project emphasizes turning simple logic into a usable tool, reinforcing the importance of clean architecture, scalability, and developer experience.

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
