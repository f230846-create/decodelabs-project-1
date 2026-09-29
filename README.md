This project is a command-line To-Do List Manager built in Python, designed to demonstrate how multiple related pieces of data can be stored, organized, and persisted using core data structures — specifically lists and dictionaries.

At its heart, the application maintains a single Python list, my_tasks, which acts as an in-memory container for all task records. Each individual task is represented as a dictionary with three keys: a unique id, the task description, and a done status flag. This mirrors the structure of a row in a database table, where the dictionary functions as the row and the list functions as the entire table — a foundational concept that scales directly into how real databases are designed.

To solve the problem of data being lost once the program terminates (since RAM is volatile), the application serializes the task list to a tasks.json file on disk every time a change is made. On startup, it automatically loads any previously saved tasks from this file, ensuring continuity across sessions.

The user interacts with the program through a simple numbered menu offering five actions:

Add Task — appends a new task dictionary to the list
View Tasks — displays all tasks with their status, using Python's enumerate() function for clean, index-aware output
Mark as Done — updates a task's completion status by its id
Delete Task — removes a task from the list by its id
Exit — safely closes the program after saving the latest data

Architecturally, the code separates Model logic (functions that add, save, load, and modify task data) from View logic (functions that handle the menu and printed output). This separation of concerns is a professional software design practice that makes the codebase easier to extend later — for example, into a graphical interface or a web application — without rewriting the underlying data logic.

Ultimately, this project trains the essential skill of storing multiple items in a single variable and managing them through structured, repeatable operations — the same underlying principle that powers data storage at scale in systems used by companies like Instagram and Google, just implemented here at an introductory level.# decodelabs-project-1
