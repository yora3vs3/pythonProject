# Basic Tuple Creation
# Tuples can hold different data types
tuple1 = (1, 2, 3)
tuple2 = ('apple', 'banana', 'cherry')
tuple3 = (True, False, True)
tuple4 = (1, "apple", 3.5)
print("tuple1:", tuple1)
print("tuple2:", tuple2)
print("tuple3:", tuple3)
print("tuple4:", tuple4)

# Single-element tuple (note the trailing comma)
single_tuple = (5,)
print("Single element tuple:", single_tuple)

# Accessing Elements
print("First element of tuple1:", tuple1[0])
print("Last element of tuple2:", tuple2[-1])

# Slicing Tuples
print("Slice of tuple1:", tuple1[1:3])  # Output: (2, 3)

# Unpacking Tuples
a, b, c = tuple1
print("Unpacked values:", a, b, c)

# Tuple unpacking with wildcard (*)
numbers = (1, 2, 3, 4, 5)
x, *y, z = numbers
print("First element:", x)
print("Middle elements:", y)
print("Last element:", z)

# Tuple Concatenation
tuple5 = tuple1 + tuple2
print("Concatenated tuple:", tuple5)

# Repeating Tuples
repeated_tuple = tuple1 * 3
print("Repeated tuple:", repeated_tuple)

# Nesting Tuples
nested_tuple = (tuple1, tuple2, tuple3)
print("Nested tuple:", nested_tuple)

# Using Tuples in a Loop
for item in tuple2:
    print("Item:", item)

# Checking if an item exists in a tuple
if 'banana' in tuple2:
    print("banana is in tuple2")

# Tuple Methods
# count(): Counts occurrences of a value
tuple6 = (1, 2, 2, 3, 4)
print("Count of 2 in tuple6:", tuple6.count(2))

# index(): Finds the index of a value
print("Index of 3 in tuple6:", tuple6.index(3))

# Functions with Tuple Return Values
def coordinates():
    return (10, 20)

x, y = coordinates()
print("Returned coordinates:", x, y)

# Using tuples as keys in a dictionary
dict_with_tuples = {("key1", "key2"): "value"}
print("Dictionary with tuple key:", dict_with_tuples)

# Tuple Comprehension Example
# Note: No direct comprehension for tuples (tuples are immutable), but we can use a generator
tuple_comprehension = tuple(i * 2 for i in range(5))
print("Tuple comprehension result:", tuple_comprehension)

# Tuple Packing and Unpacking with Function Arguments
def print_person(name, age):
    print("Name:", name)
    print("Age:", age)

person_tuple = ("Alice", 30)
print_person(*person_tuple)  # Unpacking tuple into function arguments

# Swapping Values Using Tuples
a, b = 10, 20
print("Before swap: a =", a, ", b =", b)
a, b = b, a
print("After swap: a =", a, ", b =", b)

# Immutable Nature of Tuples
try:
    tuple1[0] = 10  # This will raise a TypeError
except TypeError as e:
    print("Error:", e)

# Converting Between Tuples and Lists
list1 = [1, 2, 3]
converted_tuple = tuple(list1)
print("Converted to tuple:", converted_tuple)

back_to_list = list(converted_tuple)
print("Converted back to list:", back_to_list)

# Tuples with Variable Length Unpacking
numbers = (1, 2, 3, 4, 5, 6)
first, *middle, last = numbers
print("First:", first)
print("Middle:", middle)
print("Last:", last)
