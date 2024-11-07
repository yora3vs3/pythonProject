# Creating sets for demonstration
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
print("Initial sets:")
print("set_a:", set_a)
print("set_b:", set_b)

# add(): Adds an element to the set
set_a.add(10)
print("After add(10):", set_a)

# clear(): Removes all the elements from the set
temp_set = set_a.copy()
temp_set.clear()
print("After clear():", temp_set)

# copy(): Returns a copy of the set
set_c = set_a.copy()
print("Copy of set_a:", set_c)

# difference(): Returns a set containing the difference
diff = set_a.difference(set_b)
print("Difference (set_a - set_b):", diff)

# difference_update(): Removes the items in this set that are also in another
set_c = set_a.copy()
set_c.difference_update(set_b)
print("After difference_update with set_b:", set_c)

# discard(): Removes the specified item without raising an error if not found
set_a.discard(3)
print("After discard(3):", set_a)

# intersection(): Returns a set that is the intersection of two sets
intersection = set_a.intersection(set_b)
print("Intersection (set_a & set_b):", intersection)

# intersection_update(): Removes items not present in another set
set_d = {4, 5, 6}
set_a.intersection_update(set_d)
print("After intersection_update with {4, 5, 6}:", set_a)

# isdisjoint(): Checks if two sets have no elements in common
print("Is set_a disjoint with set_b?", set_a.isdisjoint(set_b))

# issubset(): Checks if one set is a subset of another
print("Is set_a a subset of set_b?", set_a.issubset(set_b))

# issuperset(): Checks if one set is a superset of another
print("Is set_b a superset of set_a?", set_b.issuperset(set_a))

# pop(): Removes and returns an arbitrary element from the set
popped_element = set_b.pop()
print("After pop() from set_b:", set_b)
print("Popped element:", popped_element)

# remove(): Removes the specified element, raises an error if not found
set_b.remove(7)
print("After remove(7) from set_b:", set_b)

# symmetric_difference(): Returns a set with elements in either set, but not both
sym_diff = set_a.symmetric_difference(set_b)
print("Symmetric difference (set_a ^ set_b):", sym_diff)

# symmetric_difference_update(): Updates the set with symmetric difference
set_a.symmetric_difference_update(set_b)
print("After symmetric_difference_update with set_b:", set_a)

# union(): Returns a set containing the union of sets
set_union = set_a.union(set_b)
print("Union of set_a and set_b:", set_union)

# update(): Updates the set with the union of this set and others
set_a.update({11, 12})
print("After update with {11, 12}:", set_a)

# Demonstrating shortcuts
# Resetting sets
set_a, set_b = {1, 2, 3}, {3, 4, 5}

# Using -= for difference_update
set_a -= set_b
print("set_a after -= set_b:", set_a)

# Using &= for intersection_update
set_a, set_b = {1, 2, 3}, {2, 3, 4}
set_a &= set_b
print("set_a after &= set_b:", set_a)

# Using ^= for symmetric_difference_update
set_a, set_b = {1, 2, 3}, {2, 3, 4}
set_a ^= set_b
print("set_a after ^= set_b:", set_a)

# Using |= for update
set_a, set_b = {1, 2, 3}, {3, 4, 5}
set_a |= set_b
print("set_a after |= set_b:", set_a)
