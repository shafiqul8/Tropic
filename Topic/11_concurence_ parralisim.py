"""
Topic 11: Concurrency & Parallelism
-----------------------------------
Python provides multiple ways to execute tasks concurrently:

1️⃣ Threading – multiple threads in a single process
2️⃣ Multiprocessing – multiple processes
3️⃣ Asyncio – asynchronous programming
"""

# 1️⃣ Threading Example
import threading
import time

def print_numbers():
    for i in range(5):
        print("Number:", i)
        time.sleep(0.5)

def print_letters():
    for letter in ['A','B','C','D','E']:
        print("Letter:", letter)
        time.sleep(0.5)

# Create threads
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

# Start threads
t1.start()
t2.start()

# Wait for threads to finish
t1.join()
t2.join()
print("Threading example finished.")

# 2️⃣ Multiprocessing Example
from multiprocessing import Process

def square_numbers():
    for i in range(5):
        print(f"Square of {i}:", i**2)
        time.sleep(0.5)

if __name__ == "__main__":
    p = Process(target=square_numbers)
    p.start()
    p.join()
    print("Multiprocessing example finished.")

# 3️⃣ Asyncio Example
import asyncio

async def async_task(name, delay):
    await asyncio.sleep(delay)
    print(f"Task {name} completed after {delay} seconds")

async def main():
    # Run tasks concurrently
    await asyncio.gather(
        async_task("A", 1),
        async_task("B", 2),
        async_task("C", 1.5)
    )

asyncio.run(main())
print("Asyncio example finished.")


#Excersice-------

#1

import threading

def print_even():
    for i in range(0,11,2):
        print("Even:", i)

def print_odd():
    for i in range(1,11,2):
        print("Odd:", i)

t1 = threading.Thread(target=print_even)
t2 = threading.Thread(target=print_odd)

t1.start()
t2.start()

t1.join()
t2.join()

#2

from multiprocessing import Process
import math

def factorial(n):
    print(f"Factorial of {n} is {math.factorial(n)}")

processes = []
for i in range(1,6):
    p = Process(target=factorial, args=(i,))
    processes.append(p)
    p.start()

for p in processes:
    p.join()

#3

from multiprocessing import Process
import math

def factorial(n):
    print(f"Factorial of {n} is {math.factorial(n)}")

processes = []
for i in range(1,6):
    p = Process(target=factorial, args=(i,))
    processes.append(p)
    p.start()

for p in processes:
    p.join()
  
