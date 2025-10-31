
"""
Topic 8: Exception Handling
---------------------------
Exceptions are runtime errors that can interrupt program execution.
Python provides a mechanism to handle exceptions gracefully using:

1️⃣ try, except
2️⃣ else
3️⃣ finally
4️⃣ Raising custom exceptions
"""

# 1️⃣ Basic try-except
try:
    x = 10 / 0  # Division by zero will raise an exception
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

# 2️⃣ Multiple Exceptions
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError:
    print("Error: Invalid input, enter a number.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
else:
    print("Division successful, result:", result)

# 3️⃣ Finally block
try:
    file = open("example.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found.")
finally:
    print("Execution finished. Cleaning up resources.")
    # file.close()  # If file was opened, close it safely

# 4️⃣ Raising Exceptions
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    elif age < 18:
        print("Minor")
    else:
        print("Adult")

check_age(20)
# check_age(-5)  # Uncomment to see the exception

# 5️⃣ Custom Exception
class CustomError(Exception):
    """Custom exception class"""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def test_custom(value):
    if value > 100:
        raise CustomError("Value cannot exceed 100")
    else:
        print("Value is fine:", value)

test_custom(50)
# test_custom(150)  # Uncomment to see the custom exception


#Excersice-_------------

#1
try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    print("Result:", a / b)
except ZeroDivisionError:
    print("Cannot divide by zero.")
except ValueError:
    print("Invalid input, enter a exception

          

#2

def check_positive(num):
    if num < 0:
        raise ValueError("Negative number not allowed")
    else:
        print("Number is positive")

check_positive(10)
# check_positive(-5)  # Uncomment to test exception

#3
class AgeError(Exception):
    pass

def validate_age(age):
    if age < 0:
        raise AgeError("Age cannot be negative")
    print("Valid age:", age)

validate_age(25)
# validate_age(-1)  # Uncomment to test
