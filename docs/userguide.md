# Student Task Manager - User Guide

## What is this app?

A simple Python console application for students to manage their tasks:
add a task, view all tasks, mark a task as completed, and delete a task.

## Setup

1. Make sure Python 3.11 or newer is installed.
2. Clone the repository:
   `git clone https://github.com/<username>/studenttaskmanager.git`
3. Go into the folder:
   `cd studenttaskmanager`

## How to run

`python main.py`

## How to use

When the app starts, you will see this menu:

```
--- Student Task Manager ---
1. Add task
2. Display tasks
3. Complete task
4. Delete task
5. Exit
```

- **Add task (1):** Type a task title and press Enter. An empty title is rejected.
- **Display tasks (2):** Shows all tasks. `[ ]` means pending, `[x]` means completed.
- **Complete task (3):** Enter the task ID shown next to the task.
- **Delete task (4):** Enter the task ID of the task you want to delete.
- **Exit (5):** Closes the app.

## Example

```
1 -> Complete DevOps assignment
2 -> [ ] 1. Complete DevOps assignment
3 -> Enter ID 1
2 -> [x] 1. Complete DevOps assignment
```

## How to run the tests

`python -m unittest discover -s tests -v`
