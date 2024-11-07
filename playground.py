import random
txt = "Hello World" [::-1]
print(txt.split())
mylist = ["a", "b", "a", "c", "c"]
mylist = len(dict.fromkeys(mylist))


# For an integer between 5 and 10
print(random.randint(5, 10))

# For a floating-point number between 5 and 10
print(random.uniform(5, 10))

txt = "hello"
data = txt[::-1]
print(data)
# Python code snippet

list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 0, 4, 5]

# Use zip to pair elements from both lists
paired_elements = zip(list1, list2)

# Use all to check if all corresponding elements are equal
are_all_equal = all(x == y for x, y in paired_elements)

print("Are all corresponding elements equal?:", are_all_equal)
