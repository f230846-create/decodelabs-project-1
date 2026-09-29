"""
Project 1: The To-Do List
DecodeLabs Industrial Training Kit — Python Programming

Concepts applied (per the training slides):
- Lists as the primitive dynamic-array structure (my_tasks = [])
- append() for O(1) inserts, and iteration with enumerate() for the
  "professional" index + value read pattern
- Dictionaries used as "table rows" -> {"id": ..., "task": ..., "done": ...}
- Persistence: serializing the in-memory list to a JSON file on disk,
  so data survives after the process ends (the "Volatile Trap" fix)
- Model (data logic) kept separate from View (the menu / print statements)
"""

import json
import os

DATA_FILE = "tasks.json"


# ----------------------------- MODEL (Data Logic) -----------------------------

def load_tasks():
    """Read the task list from disk. Returns [] if no file exists yet."""
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


def save_tasks(my_tasks):
    """Persist the current list to disk (RAM -> Disk)."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(my_tasks, f, indent=2)


def add_task(my_tasks, description):
    """Append a new task dict to the list. Amortized O(1)."""
    new_id = (my_tasks[-1]["id"] + 1) if my_tasks else 1
    task = {"id": new_id, "task": description.strip(), "done": False}
    my_tasks.append(task)
    return task


def complete_task(my_tasks, task_id):
    """Mark a task done by its id. Returns True if found."""
    for task in my_tasks:
        if task["id"] == task_id:
            task["done"] = True
            return True
    return False


def delete_task(my_tasks, task_id):
    """Remove a task by its id. Returns True if found."""
    for task in my_tasks:
        if task["id"] == task_id:
            my_tasks.remove(task)
            return True
    return False


# ----------------------------- VIEW (User Interface) -----------------------------

def print_menu():
    print("\n===== TO-DO LIST =====")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as done")
    print("4. Delete task")
    print("5. Exit")


def print_tasks(my_tasks):
    if not my_tasks:
        print("\n(no tasks yet — add one!)")
        return
    print("\nYour tasks:")
    for index, task in enumerate(my_tasks, start=1):
        status = "✔" if task["done"] else " "
        print(f"  [{status}] {index}. (id {task['id']}) {task['task']}")


# ----------------------------- CONTROLLER -----------------------------

def main():
    my_tasks = load_tasks()

    while True:
        print_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            description = input("Enter task description: ")
            if description.strip():
                task = add_task(my_tasks, description)
                save_tasks(my_tasks)
                print(f"Added: \"{task['task']}\" (id {task['id']})")
            else:
                print("Task description can't be empty.")

        elif choice == "2":
            print_tasks(my_tasks)

        elif choice == "3":
            print_tasks(my_tasks)
            try:
                task_id = int(input("Enter task id to mark as done: "))
            except ValueError:
                print("Please enter a valid number.")
                continue
            if complete_task(my_tasks, task_id):
                save_tasks(my_tasks)
                print("Task marked as done.")
            else:
                print("No task found with that id.")

        elif choice == "4":
            print_tasks(my_tasks)
            try:
                task_id = int(input("Enter task id to delete: "))
            except ValueError:
                print("Please enter a valid number.")
                continue
            if delete_task(my_tasks, task_id):
                save_tasks(my_tasks)
                print("Task deleted.")
            else:
                print("No task found with that id.")

        elif choice == "5":
            print("Goodbye! Your tasks are saved in tasks.json.")
            break

        else:
            print("Invalid option, please choose 1-5.")


if __name__ == "__main__":
    main()