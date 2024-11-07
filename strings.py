# capitalize()
text = "hello world"
print(text.capitalize())  # Output: "Hello world"

# center()
print(text.center(20, '-'))  # Output: "----hello world----"

# count()
print(text.count("l"))  # Output: 3 (counts occurrences of 'l')

# find()
print(text.find("world"))  # Output: 6 (starting index of substring 'world')

# join()
print("-".join(["2023", "11", "07"]))  # Output: "2023-11-07"

# replace()
print(text.replace("world", "Python"))  # Output: "hello Python"

# split()
print(text.split())  # Output: ["hello", "world"] (splits by spaces)

# strip()
text_with_spaces = "  Hello  "
print(text_with_spaces.strip())  # Output: "Hello" (removes leading and trailing spaces)

# title()
print(text.title())  # Output: "Hello World" (capitalizes first letter of each word)

# zfill()
print("42".zfill(5))  # Output: "00042" (pads string with zeros to width of 5)
