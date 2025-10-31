"""
Topic 4: Data Structures
------------------------
Python provides several built-in data structures to store and organize data.

1️⃣ List
2️⃣ Tuple
3️⃣ Set
4️⃣ Dictionary

We’ll explore each with examples, methods, and exercises.
"""

# 1️⃣ LIST
print("----- LIST -----")
# A list is an ordered, mutable collection of items.
fruits = ["apple", "banana", "cherry"]
print("Original List:", fruits)

# Access elements
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Add elements
fruits.append("orange")
print("After append:", fruits)

# Insert at a specific position
fruits.insert(1, "kiwi")
print("After insert:", fruits)

# Remove elements
fruits.remove("banana")
print("After remove:", fruits)

# Loop through list
print("Looping through list:")
for fruit in fruits:
    print(fruit)

# List comprehension
squared_numbers = [x**2 for x in range(1,6)]
print("Squared Numbers:", squared_numbers)

# 2️⃣ TUPLE
print("\n----- TUPLE -----")
# A tuple is ordered but immutable.
colors = ("red", "green", "blue")
print("Tuple:", colors)

# Access elements
print("First color:", colors[0])

# Cannot modify a tuple
# colors[0] = "yellow"  # ❌ This will raise an error

# 3️⃣ SET
print("\n----- SET -----")
# A set is unordered and contains unique items.
numbers = {1, 2, 3, 2, 4}
print("Set (duplicates removed):", numbers)

# Add elements
numbers.add(5)
print("After add:", numbers)

# Remove elements
numbers.discard(2)
print("After discard:", numbers)

# Loop through set
print("Looping through set:")
for num in numbers:
    print(num)

# 4️⃣ DICTIONARY
print("\n----- DICTIONARY -----")
# A dictionary stores key-value pairs.
student = {"name": "Sha", "age": 25, "course": "Python"}
print("Original Dictionary:", student)

# Access values
print("Student name:", student["name"])
print("Student age:", student.get("age"))

# Add or update
student["grade"] = "A"
student["age"] = 26
print("Updated Dictionary:", student)

# Remove key
student.pop("course")
print("After pop:", student)

# Loop through dictionary
print("Loop through dictionary:")
for key, value in student.items():
    print(f"{key}: {value}")

# 5️⃣ Nested Data Structures
nested = {
    "student1": {"name": "Alice", "age": 21},
    "student2": {"name": "Bob", "age": 22}
}
print("\nNested Dictionary Example:", nested)
print("Student2 name:", nested["student2"]["name"])

#Excersice Section------------------------
#1
numbers = [1, 2, 3, 4, 5]
even_numbers = [num for num in numbers if num % 2 == 0]
print("Even numbers:", even_numbers)

#2
students = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78
}
for name, marks in students.items():
    print(f"{name}: {marks}")

#3
numbers = {1, 3, 5, 7, 9}
numbers.add(11)
numbers.discard(3)
print("Final Set:", numbers)
