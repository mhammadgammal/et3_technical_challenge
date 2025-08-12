import json
import os
import datetime
import argparse

TASKS_FILE_NAME = 'tasks.json'

# task operations
def load_tasks():
    if not os.path.exists(TASKS_FILE_NAME):
        return []
    else:
        with open(TASKS_FILE_NAME, 'r') as f:
            return json.load(f)

def save_tasks(tasks):
    with open(TASKS_FILE_NAME, 'w') as f:
        json.dump(tasks, f, indent=4)

def add_task(description, priority=None, tags=None):
    tasks = load_tasks()
    tasks.append({
        "description": description,
        "done": False,
        "created_at": datetime.datetime.now().isoformat(),
        "priority": priority,
        "tags": tags or []
    })
    save_tasks(tasks)
    print(f"Task added: {description}")

def delete_task(index):
    tasks = load_tasks()
    try:
        removed = tasks.pop(index-1)
        save_tasks(tasks)
        print(f"Deleted task: {removed['description']}")
    except IndexError:
        print("Invalid task number.")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
    else:
        for task in tasks:
            print(f"Task: {task['name']}, Status: {task['status']}")

def mark_done(index):
    tasks = load_tasks()
    try:
        tasks[index-1]["done"] = True
        save_tasks(tasks)
        print(f"Task #{index} marked as done.")
    except IndexError:
        print("Invalid task number.")