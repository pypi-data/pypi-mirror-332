# Todo CLI

A simple command-line interface (CLI) application to manage your todo list.

<video controls>
    <source src="./demo.mp4" />
</video>


## Features

- Add new tasks
- List all tasks
- Mark tasks as completed
- Delete tasks

## Installation

Install the package:

```bash
pip install cli-todo
```

### To-Do List Commands

#### ➕ Add a New Task
```sh
C:\User> uv run python main.py add
Task: Buy grocery for sehri and iftari
Task added: Buy grocery for sehri and iftari
```

#### 📜 List All Tasks
```sh
C:\User> uv run python main.py list
0. Buy grocery for sehri and iftari [❌]
```

#### ✅ Mark a Task as Completed
```sh
C:\User> uv run python main.py complete
[?] Select task to mark as completed:
 > Buy grocery for sehri and iftari

Task: "Buy grocery for sehri and iftari" marked as completed.
```

#### ❌ Remove a Task
```sh
C:\User> uv run python main.py remove
[?] Select task to remove:
 > 0. Buy grocery for sehri and iftari [✅]

Task: "Buy grocery for sehri and iftari" removed.
```
