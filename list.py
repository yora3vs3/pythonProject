# Sample list
my_list = [1, 2, 3, 4, 5]

# append(): Adds an element at the end of the list
my_list.append(6)
print("After append(6):", my_list)  # Output: [1, 2, 3, 4, 5, 6]

# clear(): Removes all elements from the list
my_list.clear()
print("After clear():", my_list)  # Output: []

# Resetting the list for other examples
my_list = [1, 2, 2, 3, 4, 5]

# copy(): Returns a copy of the list
list_copy = my_list.copy()
print("Copy of list:", list_copy)  # Output: [1, 2, 2, 3, 4, 5]

# count(): Returns the number of elements with the specified value
print("Count of 2 in my_list:", my_list.count(2))  # Output: 2

# extend(): Adds elements from another list (or any iterable) to the end of the current list
my_list.extend([6, 7, 8])
print("After extend([6, 7, 8]):", my_list)  # Output: [1, 2, 2, 3, 4, 5, 6, 7, 8]

# index(): Returns the index of the first element with the specified value
print("Index of first occurrence of 3:", my_list.index(3))  # Output: 3

# insert(): Adds an element at the specified position
my_list.insert(2, "new")
print("After insert(2, 'new'):", my_list)  # Output: [1, 2, 'new', 2, 3, 4, 5, 6, 7, 8]

# pop(): Removes the element at the specified position (last element if no index specified)
my_list.pop(2)
print("After pop(2):", my_list)  # Output: [1, 2, 2, 3, 4, 5, 6, 7, 8]

# remove(): Removes the first item with the specified value
my_list.remove(2)
print("After remove(2):", my_list)  # Output: [1, 2, 3, 4, 5, 6, 7, 8]

# reverse(): Reverses the order of the list
my_list.reverse()
print("After reverse():", my_list)  # Output: [8, 7, 6, 5, 4, 3, 2, 1]

# sort(): Sorts the list (ascending by default)
my_list.sort()
print("After sort():", my_list)  # Output: [1, 2, 3, 4, 5, 6, 7, 8]

# Sorting in descending order
my_list.sort(reverse=True)
print("After sort(reverse=True):", my_list)  # Output: [8, 7, 6, 5, 4, 3, 2, 1]
