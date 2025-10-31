"""
Topic 13: Final Project Examples & Integration
-----------------------------------------------
This topic combines all Python skills learned so far to create small 
portfolio-ready projects.

Examples include:
1️⃣ CLI Tool: Task Manager
2️⃣ File-based Mini Database: Student Management
3️⃣ Integration Example: API + File + Logging
"""

# 1️⃣ CLI Task Manager
# Features: Add task, View tasks, Mark done
import json

TASK_FILE = "tasks.json"

def load_tasks():
    try:
        with open(TASK_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def add_task(task_name):
    tasks = load_tasks()
    tasks.append({"task": task_name, "done": False})
    save_tasks(tasks)
    print(f"Task '{task_name}' added.")

def view_tasks():
    tasks = load_tasks()
    for i, t in enumerate(tasks, 1):
        status = "Done" if t["done"] else "Pending"
        print(f"{i}. {t['task']} [{status}]")

def mark_done(task_number):
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        tasks[task_number-1]["done"] = True
        save_tasks(tasks)
        print(f"Task {task_number} marked as done.")
    else:
        print("Invalid task number")

# Example Usage
add_task("Learn Python")
add_task("Build Portfolio Project")
view_tasks()
mark_done(1)
view_tasks()

# 2️⃣ Student Management (File-based)
STUDENT_FILE = "students.json"

def add_student(name, age, course):
    try:
        students = load_students()
    except:
        students = []
    students.append({"name": name, "age": age, "course": course})
    save_students(students)
    print(f"Student {name} added.")

def load_students():
    try:
        with open(STUDENT_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_students(students):
    with open(STUDENT_FILE, "w") as f:
        json.dump(students, f, indent=2)

def view_students():
    students = load_students()
    for s in students:
        print(f"{s['name']} | Age: {s['age']} | Course: {s['course']}")

# Example Usage
add_student("Alice", 21, "Python")
add_student("Bob", 22, "Data Science")
view_students()

# 3️⃣ Integration Example: API + File + Logging
import logging
import requests

logging.basicConfig(level=logging.INFO)

def fetch_api_data(url, filename):
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        with open(filename, "w") as f:
            json.dump(data, f, indent=2)
        logging.info(f"Data saved to {filename}")
    except requests.RequestException as e:
        logging.error(f"API request failed: {e}")

# Example Usage (Uncomment to run)
# fetch_api_data("https://jsonplaceholder.typicode.com/todos", "todos.json")
