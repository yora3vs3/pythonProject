from string import Template

# Basic `str.format()` Examples
name = "Alice"
age = 30
height = 5.7

# Basic usage
intro = "My name is {} and I am {} years old.".format(name, age)
print(intro)

# Using index numbers
intro_repeated = "Name: {0}, Age: {1}, Height: {2}, Again Name: {0}".format(name, age, height)
print(intro_repeated)

# Named placeholders
intro_named = "My name is {name} and my age is {age}".format(name="Bob", age=25)
print(intro_named)

# F-strings Examples
print("\n--- F-strings Examples ---")

# Basic f-string
intro_fstring = f"My name is {name} and I am {age} years old and {height} feet tall."
print(intro_fstring)

# Expressions in f-strings
print(f"Next year, {name} will be {age + 1} years old.")

# Formatting Numbers
number = 1234567.89123

print("\n--- Number Formatting ---")
print(f"With comma separator: {number:,}")
print(f"Rounded to 2 decimal places: {number:.2f}")
print(f"Scientific notation: {number:.2e}")

percentage = 0.0734
print(f"As percentage: {percentage:.2%}")

# Padding and Alignment
print("\n--- Padding and Alignment ---")
width = 10

# Left, Right, Center Alignment
print(f"{name:<{width}}: ${height}")
print(f"{name:>{width}}: ${height}")
print(f"{name:^{width}}: ${height}")

# Zero padding
print(f"{height:010.2f}")

# Formatting with Dictionaries and Lists
print("\n--- Formatting with Dictionaries and Lists ---")
book = {"title": "Python Programming", "author": "John Doe", "price": 29.99}
print("Using dictionary with `str.format()`: " + "Title: {title}, Author: {author}, Price: ${price:.2f}".format(**book))
print(f"Using dictionary with f-strings: Title: {book['title']}, Author: {book['author']}, Price: ${book['price']:.2f}")

# Using List with formatting
values = [10, 20, 30]
print("Values using `str.format()`: {} {} {}".format(values[0], values[1], values[2]))
print(f"Values using f-strings: {values[0]} {values[1]} {values[2]}")

# Escaping Braces
print("\n--- Escaping Braces ---")
value = 42
print("To show braces, use double braces: {{value}} which gives {value}".format(value=value))

# Complex Formatting Example
print("\n--- Complex Formatting Example ---")
products = [
    {"name": "Laptop", "price": 899.99, "stock": 25},
    {"name": "Phone", "price": 499.99, "stock": 50},
    {"name": "Tablet", "price": 299.99, "stock": 0},
]

header = f"{'Product':<15}{'Price':>10}{'Stock':>10}"
print(header)
print("-" * len(header))

for product in products:
    name = product["name"]
    price = product["price"]
    stock = product["stock"]

    stock_status = "In Stock" if stock > 0 else "Out of Stock"
    print(f"{name:<15}${price:>9,.2f}{stock_status:>12}")

average_price = sum(p['price'] for p in products) / len(products)
print("\nAverage Price of Products: ${:.2f}".format(average_price))

# Advanced Formatting with Custom Classes
print("\n--- Advanced Formatting with Custom Classes ---")


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __format__(self, format_spec):
        if format_spec == "detailed":
            return f"{self.name} costs ${self.price:.2f}"
        elif format_spec == "brief":
            return f"{self.name} (${self.price})"
        else:
            return str(self)


product = Product("Smart Watch", 199.99)
print(f"{product:detailed}")
print(f"{product:brief}")

# Template Strings
print("\n--- Template Strings ---")
template = Template("Hello, $name! You have $$${balance} in your account.")
message = template.substitute(name="Alice", balance="50.00")
print(message)

# Legacy `%` Formatting
print("\n--- Legacy `%` Formatting ---")
name = "Alice"
age = 30
price = 45.6789

# Using `%` for String, Integer, and Float substitution
print("Name: %s, Age: %d" % (name, age))
print("Price: %.2f" % price)
print("Name: %s, Age: %d, Price: %.2f" % (name, age, price))

# Combining all string formatting types for a comprehensive overview
print("\n--- Combined Formatting Overview ---")

# F-string, `str.format()`, Template, and `%` formatting in a single code block
title = "Ultimate Guide to Python"
author = "John Doe"
price = 49.99

print(f"F-string: Title: {title}, Author: {author}, Price: ${price:.2f}")
print("str.format(): Title: {}, Author: {}, Price: ${:.2f}".format(title, author, price))

template = Template("Template: Title: $title, Author: $author, Price: $$${price}")
message = template.substitute(title=title, author=author, price=price)
print(message)

print("Legacy %: Title: %s, Author: %s, Price: $%.2f" % (title, author, price))
