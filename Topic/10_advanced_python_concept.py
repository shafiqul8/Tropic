"""
Topic 10: Advanced Python Concepts
----------------------------------
In this topic, we cover advanced features of Python:

1️⃣ Decorators
2️⃣ Generators
3️⃣ Iterators
4️⃣ List Comprehensions
5️⃣ Regular Expressions (Regex)
6️⃣ Type Hinting
"""

# 1️⃣ Decorators
def decorator_function(func):
    """A simple decorator example"""
    def wrapper():
        print("Before function execution")
        func()
        print("After function execution")
    return wrapper

@decorator_function  # Using decorator
def say_hello():
    print("Hello, Python!")

say_hello()

# 2️⃣ Generators
def my_generator(n):
    """Generator yields numbers from 0 to n-1"""
    for i in range(n):
        yield i

gen = my_generator(5)
print("Generator output:")
for num in gen:
    print(num)

# 3️⃣ Iterators
my_list = [10, 20, 30]
it = iter(my_list)
print("\nIterator output:")
print(next(it))  # 10
print(next(it))  # 20
print(next(it))  # 30
# print(next(it))  # StopIteration error

# 4️⃣ List Comprehensions
nums = [1, 2, 3, 4, 5]
squared = [x**2 for x in nums]
even = [x for x in nums if x % 2 == 0]
print("\nList Comprehensions:")
print("Squared:", squared)
print("Even:", even)

# 5️⃣ Regular Expressions (Regex)
import re
text = "My phone number is 123-456-7890"
pattern = r"\d{3}-\d{3}-\d{4}"
match = re.search(pattern, text)
if match:
    print("\nRegex match found:", match.group())

# 6️⃣ Type Hinting
def add_numbers(a: int, b: int) -> int:
    """Adds two integers and returns an integer"""
    return a + b

result = add_numbers(5, 10)
print("\nType Hinting Example Result:", result)


#3 Excersice---------

#1
def my_decorator(func):
    def wrapper():
        print("Start")
        func()
        print("End")
    return wrapper

@my_decorator
def greet():
    print("Hello!")

greet()

#2

def even_generator(n):
    for i in range(n+1):
        if i % 2 == 0:
            yield i

for num in even_generator(10):
    print(num)

#3
import re
text = "Contact: alice@example.com, bob@test.org"
emails = re.findall(r'\S+@\S+', text)
print("Emails found:", emails)


#4

squares = [x**2 for x in range(1,21) if x % 3 == 0]
print("Squares divisible by 3:", squares)
