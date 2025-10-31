"""
Topic 2: Operators & Expressions
--------------------------------
In this section, you'll learn about all Python operators:
    - Arithmetic Operators
    - Comparison Operators
    - Logical Operators
    - Assignment Operators
    - Membership Operators
    - Identity Operators
Each example includes explanations and outputs.
"""

# 1️⃣ Arithmetic Operators
a = 10
b = 3

print("Addition:", a + b)        # 13
print("Subtraction:", a - b)     # 7
print("Multiplication:", a * b)  # 30
print("Division:", a / b)        # 3.333...
print("Floor Division:", a // b) # 3
print("Modulus:", a % b)         # 1
print("Exponent:", a ** b)       # 1000

# 2️⃣ Comparison Operators
print("\nComparison Operators:")
print("a == b:", a == b)  # False
print("a != b:", a != b)  # True
print("a > b:", a > b)    # True
print("a < b:", a < b)    # False

# 3️⃣ Logical Operators
x = True
y = False

print("\nLogical Operators:")
print("x and y:", x and y)  # False
print("x or y:", x or y)    # True
print("not x:", not x)      # False

# 4️⃣ Assignment Operators
num = 10
print("\nAssignment Operators:")
num += 5   # num = num + 5
print("num += 5 →", num)

num *= 2   # num = num * 2
print("num *= 2 →", num)

num //= 3  # num = num // 3
print("num //= 3 →", num)

# 5️⃣ Membership Operators
fruits = ["apple", "banana", "cherry"]
print("\nMembership Operators:")
print("'apple' in fruits:", "apple" in fruits)     # True
print("'grape' not in fruits:", "grape" not in fruits) # True

# 6️⃣ Identity Operators
x = [1, 2, 3]
y = [1, 2, 3]
z = x

print("\nIdentity Operators:")
print("x is y:", x is y)     # False (different objects)
print("x == y:", x == y)     # True (same values)
print("x is z:", x is z)     # True (same object)

# 7️⃣ Expression Example
# Combine multiple operators to form expressions
result = (a + b) * (a - b) / b
print("\nExpression Result:", result)
