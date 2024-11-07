# Sample dictionary
my_dict = {"name": "Alice", "age": 25, "city": "New York"}

# clear(): Removes all elements from the dictionary
my_dict.clear()
print("After clear():", my_dict)  # Output: {}

# Resetting the dictionary for other examples
my_dict = {"name": "Alice", "age": 25, "city": "New York"}

# copy(): Returns a copy of the dictionary
dict_copy = my_dict.copy()
print("Copy of dictionary:", dict_copy)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}

# fromkeys(): Creates a dictionary with specified keys and a single value
keys = ["a", "b", "c"]
new_dict = dict.fromkeys(keys, 0)
print("Dictionary from keys with value 0:", new_dict)  # Output: {'a': 0, 'b': 0, 'c': 0}

# get(): Returns the value for the specified key, or None if key is not found
print("Value of 'name':", my_dict.get("name"))  # Output: Alice
print("Value of 'job' (not found):", my_dict.get("job"))  # Output: None

# items(): Returns a view object with key-value pairs as tuples
print("Items:", my_dict.items())  # Output: dict_items([('name', 'Alice'), ('age', 25), ('city', 'New York')])

# keys(): Returns a view object of all keys in the dictionary
print("Keys:", my_dict.keys())  # Output: dict_keys(['name', 'age', 'city'])

# pop(): Removes and returns the value for the specified key
age = my_dict.pop("age")
print("Popped 'age':", age)  # Output: 25
print("Dictionary after pop():", my_dict)  # Output: {'name': 'Alice', 'city': 'New York'}

# popitem(): Removes and returns the last inserted key-value pair
last_item = my_dict.popitem()
print("Last item removed:", last_item)  # Output: ('city', 'New York')
print("Dictionary after popitem():", my_dict)  # Output: {'name': 'Alice'}

# setdefault(): Returns the value of a key if it exists; if not, adds the key with the specified value
age_value = my_dict.setdefault("age", 30)
print("setdefault for 'age':", age_value)  # Output: 30 (age is added since it wasn't in the dictionary)
print("Dictionary after setdefault():", my_dict)  # Output: {'name': 'Alice', 'age': 30}

# update(): Updates the dictionary with new key-value pairs
my_dict.update({"city": "Los Angeles", "job": "Engineer"})
print("Dictionary after update():", my_dict)  # Output: {'name': 'Alice', 'age': 30, 'city': 'Los Angeles', 'job': 'Engineer'}

# values(): Returns a view object with all values in the dictionary
print("Values:", my_dict.values())  # Output: dict_values(['Alice', 30, 'Los Angeles', 'Engineer'])
