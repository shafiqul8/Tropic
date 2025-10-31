"""
Topic 6: Object-Oriented Programming (OOP)
------------------------------------------
OOP is a programming paradigm based on the concept of objects.
Python supports OOP with:
1️⃣ Classes & Objects
2️⃣ Attributes & Methods
3️⃣ Inheritance
4️⃣ Polymorphism
5️⃣ Encapsulation
"""

# 1️⃣ Basic Class and Object
class Person:
    """A class to represent a person"""
    def __init__(self, name, age):
        # __init__ is the constructor
        self.name = name
        self.age = age

    def greet(self):
        """Method to greet"""
        return f"Hello, my name is {self.name} and I am {self.age} years old."

# Creating object
p1 = Person("Sha", 25)
print(p1.greet())

# 2️⃣ Instance vs Class Variables
class Student:
    school = "XYZ School"  # Class variable

    def __init__(self, name, age):
        self.name = name   # Instance variable
        self.age = age

s1 = Student("Alice", 21)
s2 = Student("Bob", 22)

print(s1.name, s1.age, s1.school)
print(s2.name, s2.age, s2.school)

# 3️⃣ Inheritance
class Employee(Person):
    """Child class inherits from Person"""
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def show_salary(self):
        return f"{self.name} earns {self.salary} USD."

e1 = Employee("John", 30, 5000)
print(e1.greet())       # Inherited method
print(e1.show_salary()) # Child method

# 4️⃣ Method Overriding (Polymorphism)
class Manager(Employee):
    def show_salary(self):
        return f"{self.name} earns {self.salary} USD + bonus."

m1 = Manager("Sara", 35, 8000)
print(m1.show_salary())

# 5️⃣ Encapsulation
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Private attribute

    # Getter method
    def get_balance(self):
        return self.__balance

    # Setter method
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid amount")

account = BankAccount("Sha", 1000)
print("Balance:", account.get_balance())
account.deposit(500)
print("Balance after deposit:", account.get_balance())
# print(account.__balance)  # ❌ This will give error (private attribute)

# 6️⃣ Class Methods and Static Methods
class Circle:
    pi = 3.14159  # Class variable

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return Circle.pi * (self.radius ** 2)

    @classmethod
    def change_pi(cls, new_pi):
        cls.pi = new_pi

    @staticmethod
    def greet():
        return "Welcome to the Circle class"

c1 = Circle(5)
print("Area:", c1.area())
print(Circle.greet())
Circle.change_pi(3.14)
print("Area after changing pi:", c1.area())

#Excersice--------

#1
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def car_info(self):
        return f"{self.year} {self.brand} {self.model}"

car1 = Car("Toyota", "Corolla", 2020)
print(car1.car_info())

#2

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

rect = Rectangle(5, 3)
print("Area:", rect.area())
print("Perimeter:", rect.perimeter())

#3

class Student:
    def __init__(self, name):
        self.name = name
        self.__marks = 0

    def set_marks(self, marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def grade(self):
        if self.__marks >= 90:
            return "A"
        elif self.__marks >= 75:
            return "B"
        elif self.__marks >= 60:
            return "C"
        else:
            return "F"

s = Student("Sha")
s.set_marks(85)
print("Marks:", s.get_marks())
print("Grade:", s.grade())
