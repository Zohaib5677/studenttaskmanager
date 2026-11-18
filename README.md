# studenttaskmanager

Project status: In Progress

# Student Task Manager

Project status: Planning

A small Python console application to add, display, complete, and delete
student tasks. Built for Lab Assignment 4, DevOps for Cloud Computing
(CSC418), COMSATS University Islamabad, Lahore Campus.

## Features

- Add a task (empty titles are rejected)
- Display all tasks with completed / pending status
- Mark a selected task as completed
- Delete a task using its task ID
- Automated tests with Python `unittest`
- GitHub Actions workflow that runs tests on push and pull requests

## Setup

1. Install Python 3.11 or newer.
2. Clone the repository:
   `git clone https://github.com/<username>/studenttaskmanager.git`
3. Go into the folder:
   `cd studenttaskmanager`

## Usage

Run the app:

`python main.py`

Then use the menu:

1. Add task
2. Display tasks
3. Complete task
4. Delete task
5. Exit

See `docs/userguide.md` for a step-by-step user guide.

## Test Instructions

Run all tests with:

`python -m unittest discover -s tests -v`

The tests cover adding a task, marking a task complete, and deleting a task.

## Project Structure

```
studenttaskmanager/
├── main.py
├── task_manager.py
├── tests/
│   └── test_task_manager.py
├── .github/workflows/test.yml
├── docs/userguide.md
├── LABREPORT.md
└── labevidence/
```

## Author

Muhammad Zohaib (SP23-BSE-137)
