"""
Topic 7: File Handling
---------------------
Python provides built-in functions to read, write, and manipulate files.
We will cover:
1️⃣ Opening and closing files
2️⃣ Reading files
3️⃣ Writing and appending files
4️⃣ Working with CSV and JSON
5️⃣ Using context managers (with statement)
"""

import json
import csv

# 1️⃣ Open a File
# Modes: 'r' (read), 'w' (write), 'a' (append), 'r+' (read/write)
file = open("example.txt", "w")  # Opens file in write mode
file.write("Hello, Python!\nThis is a file handling example.")
file.close()  # Always close files to save changes

# 2️⃣ Read a File
file = open("example.txt", "r")
content = file.read()  # Reads entire file
print("File Content:\n", content)
file.close()

# Read line by line
file = open("example.txt", "r")
print("\nReading line by line:")
for line in file:
    print(line.strip())  # strip() removes newline
file.close()

# 3️⃣ Append to a File
file = open("example.txt", "a")
file.write("\nThis line is appended.")
file.close()

# Verify appended content
with open("example.txt", "r") as f:
    print("\nAfter Append:\n", f.read())

# 4️⃣ Using Context Managers
# Automatically closes the file after the block
with open("example2.txt", "w") as f:
    f.write("This is written using a context manager.")

with open("example2.txt", "r") as f:
    print("\nContext Manager Read:\n", f.read())

# 5️⃣ Working with CSV Files
# Writing CSV
data = [["Name", "Age"], ["Alice", 21], ["Bob", 22]]
with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)

# Reading CSV
with open("data.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print("CSV Row:", row)

# 6️⃣ Working with JSON Files
person = {"name": "Sha", "age": 25, "course": "Python"}

# Write JSON to file
with open("person.json", "w") as f:
    json.dump(person, f)

# Read JSON from file
with open("person.json", "r") as f:
    data = json.load(f)
    print("\nJSON Data:", data)

#Excersice----------

#1
with open("my_info.txt", "w") as f:
    f.write("Name: Sha\nAge: 25")

with open("my_info.txt", "r") as f:
    print(f.read())

#2

import csv

students = [["Name", "Marks"], ["Alice", 85], ["Bob", 90], ["Charlie", 78]]

# Write CSV
with open("students.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(students)

# Read CSV
with open("students.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

  #3
  import json

data = {"course": "Python", "level": "Intermediate"}
with open("course.json", "w") as f:
    json.dump(data, f)

with open("course.json", "r") as f:
    loaded_data = json.load(f)
    print(loaded_data)
