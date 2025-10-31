"""
Topic 5: Functions
------------------
Functions are blocks of reusable code that perform a specific task.
They help make code modular, readable, and maintainable.

We will cover:
1️⃣ Defining functions
2️⃣ Function arguments (positional, keyword, default, variable-length)
3️⃣ Return values
4️⃣ Lambda functions
5️⃣ Map, Filter, Reduce
6️⃣ Recursion
"""

# 1️⃣ Basic Function
def greet(name):
    """Function to greet a person by name"""
    return f"Hello, {name}!"

print(greet("Sha"))  # Output: Hello, Sha!

# 2️⃣ Function with Multiple Arguments
def add(a, b):
    """Function to add two numbers"""
    return a + b

print("Sum:", add(10, 5))

# 3️⃣ Default Arguments
def greet_with_age(name, age=25):
    """Function with default age"""
    return f"{name} is {age} years old"

print(greet_with_age("Sha"))        # Uses default age
print(greet_with_age("Alice", 30))  # Overrides default age

# 4️⃣ Keyword Arguments
def student_info(name, age):
    print(f"Name: {name}, Age: {age}")

student_info(age=22, name="Bob")  # Arguments can be passed by keyword

# 5️⃣ Variable-Length Arguments
def sum_all(*numbers):
    """Accepts any number of arguments and returns their sum"""
    total = 0
    for num in numbers:
        total += num
    return total

print("Sum of numbers:", sum_all(1,2,3,4,5))

# 6️⃣ Lambda Functions (Anonymous Functions)
square = lambda x: x**2
print("Square of 5:", square(5))

# 7️⃣ Map Function Example
nums = [1,2,3,4,5]
squared = list(map(lambda x: x**2, nums))
print("Squared Numbers using map:", squared)

# 8️⃣ Filter Function Example
even_numbers = list(filter(lambda x: x % 2 == 0, nums))
print("Even Numbers using filter:", even_numbers)

# 9️⃣ Reduce Function Example
from functools import reduce
total_sum = reduce(lambda a, b: a + b, nums)
print("Total sum using reduce:", total_sum)

# 🔟 Recursion Example
def factorial(n):
    """Recursively calculates factorial"""
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print("Factorial of 5:", factorial(5))

#Excersice--------

#1
def max_in_list(numbers):
    return max(numbers)

print(max_in_list([3, 7, 2, 9, 5]))

#2
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

print(is_prime(17))  # True
print(is_prime(20))  # False

#3
celsius = [0, 20, 30, 100]
fahrenheit = list(map(lambda c: (c*9/5)+32, celsius))
print(fahrenheit)
