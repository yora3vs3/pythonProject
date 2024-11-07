# and: Logical operator
x, y = True, False
print("x and y:", x and y)

# as: Create an alias
import math as m
print("Square root using alias:", m.sqrt(16))

# assert: For debugging
n = 5
assert n > 0, "n is not positive"

# break: Break out of a loop
for i in range(5):
    if i == 3:
        break
    print("break example:", i)

# class: Define a class
class Dog:
    def bark(self):
        print("Woof!")

my_dog = Dog()
my_dog.bark()

# continue: Continue to the next iteration of a loop
for i in range(5):
    if i == 2:
        continue
    print("continue example:", i)

# def: Define a function
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))

# del: Delete an object
x = [1, 2, 3]
del x[1]
print("After del:", x)

# elif, else: Conditional statements
num = 10
if num > 10:
    print("Greater than 10")
elif num == 10:
    print("Equals 10")
else:
    print("Less than 10")

# except: Handle exceptions
try:
    1 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")

# False: Boolean value
print("False is:", False)

# finally: Block executed no matter what
try:
    x = 1 / 0
except ZeroDivisionError:
    print("Exception occurred")
finally:
    print("This always runs")

# for: Create a for loop
for i in range(3):
    print("for loop:", i)

# from: Import specific parts of a module
from math import pi
print("PI:", pi)

# global: Declare a global variable
def set_global():
    global z
    z = 20

set_global()
print("Global variable z:", z)

# if: Conditional statement
if True:
    print("if condition is True")

# import: Import a module
import random
print("Random number:", random.randint(1, 10))

# in: Check if value is in a list
print("3 in list:", 3 in [1, 2, 3])

# is: Test if two variables are equal
a = None
print("a is None:", a is None)

# lambda: Create an anonymous function
square = lambda x: x * x
print("Square using lambda:", square(4))

# None: Represents null value
nothing = None
print("None value:", nothing)

# nonlocal: Declare a non-local variable
def outer():
    x = "outer"
    def inner():
        nonlocal x
        x = "inner"
    inner()
    print("nonlocal example:", x)

outer()

# not: Logical operator
print("not True:", not True)

# or: Logical operator
print("True or False:", True or False)

# pass: Null statement
def do_nothing():
    pass

# raise: Raise an exception
try:
    raise ValueError("An error occurred")
except ValueError as e:
    print("Exception raised:", e)

# return: Exit a function and return a value
def add(a, b):
    return a + b

print("Return example:", add(2, 3))

# True: Boolean value
print("True is:", True)

# try: Exception handling
try:
    x = int("not a number")
except ValueError:
    print("ValueError occurred")

# while: Create a while loop
count = 0
while count < 3:
    print("while loop:", count)
    count += 1

# with: Simplify exception handling with file operations
with open("example.txt", "w") as f:
    f.write("Hello, with!")

# yield: Return from a generator
def generate_numbers():
    for i in range(3):
        yield i

print("Yield example:", list(generate_numbers()))
a