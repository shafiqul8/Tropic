"""
Topic 9: Modules & Packages
---------------------------
Modules are Python files containing functions, variables, and classes.
Packages are directories containing multiple modules.

We will cover:
1️⃣ Importing built-in modules
2️⃣ Creating and importing custom modules
3️⃣ Using packages
"""

# 1️⃣ Importing Built-in Modules
import math
import random
import datetime

# Math module
print("Square root of 16:", math.sqrt(16))
print("Pi value:", math.pi)

# Random module
print("Random integer between 1 and 10:", random.randint(1, 10))
print("Random choice from list:", random.choice(["apple", "banana", "cherry"]))

# Datetime module
now = datetime.datetime.now()
print("Current date and time:", now)
print("Year:", now.year, "Month:", now.month, "Day:", now.day)

# 2️⃣ Importing Specific Functions
from math import factorial, pow
print("Factorial of 5:", factorial(5))
print("2 raised to 3:", pow(2, 3))

# 3️⃣ Alias Modules
import math as m
print("Cosine of 0:", m.cos(0))

# 4️⃣ Creating a Custom Module
# Suppose we have a file named my_module.py with the following content:
# def greet(name):
#     return f"Hello, {name}!"
# def add(a, b):
#     return a + b

# Then we can import it
# import my_module
# print(my_module.greet("Sha"))
# print(my_module.add(5, 3))

# 5️⃣ From Custom Module Import Specific Functions
# from my_module import greet
# print(greet("Alice"))

# 6️⃣ Using Packages
# A package is a folder with __init__.py file
# Example structure:
# my_package/
#   __init__.py
#   module1.py
#   module2.py
# Then you can import:
# from my_package.module1 import some_function


#Excersice------------

#1
# calculator.py
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"

# main.py
import calculator
print(calculator.add(5, 3))
print(calculator.divide(10, 2))

#2

import random
for i in range(5):
    print("Dice roll:", random.randint(1,6))


#3
import datetime
now = datetime.datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))
