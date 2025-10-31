"""
Topic 3: Conditional Statements & Loops
----------------------------------------
Python provides decision-making and looping structures that control 
the flow of execution. In this section, you’ll learn:

1️⃣ Conditional statements (if, elif, else)
2️⃣ Nested if statements
3️⃣ Looping (for, while)
4️⃣ Loop control statements (break, continue, pass)
5️⃣ Real examples and exercises
"""

# 1️⃣ IF, ELIF, ELSE Example
age = 20

if age < 13:
    print("You are a child.")
elif age < 20:
    print("You are a teenager.")
else:
    print("You are an adult.")

# 2️⃣ Nested IF Example
marks = 85

if marks >= 60:
    if marks >= 80:
        print("Grade: A")
    else:
        print("Grade: B")
else:
    print("Fail")

# 3️⃣ FOR Loop Example
print("\nFor Loop Example:")
for i in range(5):
    print("Iteration:", i)

# 4️⃣ WHILE Loop Example
print("\nWhile Loop Example:")
count = 0
while count < 5:
    print("Count:", count)
    count += 1

# 5️⃣ BREAK Statement
print("\nBreak Example:")
for num in range(1, 10):
    if num == 5:
        break  # Stop loop when 5 is reached
    print(num)

# 6️⃣ CONTINUE Statement
print("\nContinue Example:")
for num in range(1, 6):
    if num == 3:
        continue  # Skip when num == 3
    print(num)

# 7️⃣ PASS Statement
print("\nPass Example:")
for i in range(3):
    pass  # Placeholder, does nothing yet
print("Pass allows an empty block without error.")

# 8️⃣ FOR Loop with LIST
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("Fruit:", fruit)

# 9️⃣ NESTED Loop Example
print("\nNested Loop Example:")
for i in range(1, 4):
    for j in range(1, 3):
        print(f"Outer: {i}, Inner: {j}")

# 🔟 RANGE with Step
print("\nRange with Step:")
for i in range(0, 10, 2):
    print(i)

# ✅ Mini Practical Example
# Sum of numbers from 1 to n using a loop
n = 5
total = 0
for i in range(1, n + 1):
    total += i
print(f"\nSum of first {n} numbers is:", total)

#Excersice----------

#1
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

#2
n = int(input("Enter a number for its table: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
