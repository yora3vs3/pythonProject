import os
import json
import csv
import pickle
from datetime import datetime

# Directory setup
if not os.path.exists("library_data"):
    os.makedirs("library_data")

# Sample data
books = [
    {"title": "1984", "author": "George Orwell", "year": 1949},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925},
]


# Writing to a text file
def write_text_file(filename, data):
    with open(f"library_data/{filename}", "w") as file:
        for book in data:
            file.write(f"{book['title']}, by {book['author']} ({book['year']})\n")
    print(f"Data written to {filename} successfully.\n")


# Reading from a text file
def read_text_file(filename):
    try:
        with open(f"library_data/{filename}", "r") as file:
            print(f"Reading from {filename}:\n")
            print(file.read())
    except FileNotFoundError:
        print(f"{filename} not found.\n")


# Writing to a JSON file
def write_json_file(filename, data):
    with open(f"library_data/{filename}", "w") as file:
        json.dump(data, file, indent=4)
    print(f"Data written to {filename} as JSON.\n")


# Reading from a JSON file
def read_json_file(filename):
    try:
        with open(f"library_data/{filename}", "r") as file:
            data = json.load(file)
            print(f"Reading from {filename}:\n{json.dumps(data, indent=4)}\n")
    except FileNotFoundError:
        print(f"{filename} not found.\n")


# Writing to a CSV file
def write_csv_file(filename, data):
    with open(f"library_data/{filename}", "w", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["title", "author", "year"])
        writer.writeheader()
        writer.writerows(data)
    print(f"Data written to {filename} as CSV.\n")


# Reading from a CSV file
def read_csv_file(filename):
    try:
        with open(f"library_data/{filename}", "r") as file:
            reader = csv.DictReader(file)
            print(f"Reading from {filename}:\n")
            for row in reader:
                print(row)
            print()
    except FileNotFoundError:
        print(f"{filename} not found.\n")


# Writing to a binary file using Pickle
def write_pickle_file(filename, data):
    with open(f"library_data/{filename}", "wb") as file:
        pickle.dump(data, file)
    print(f"Data written to {filename} as a binary Pickle file.\n")


# Reading from a binary file using Pickle
def read_pickle_file(filename):
    try:
        with open(f"library_data/{filename}", "rb") as file:
            data = pickle.load(file)
            print(f"Reading from {filename}:\n{data}\n")
    except FileNotFoundError:
        print(f"{filename} not found.\n")


# Appending data to a text file
def append_text_file(filename, data):
    with open(f"library_data/{filename}", "a") as file:
        for book in data:
            file.write(f"{book['title']}, by {book['author']} ({book['year']})\n")
    print(f"Data appended to {filename} successfully.\n")


# Using seek to navigate within a file
def demonstrate_seek(filename):
    try:
        with open(f"library_data/{filename}", "r") as file:
            print("Reading first 20 characters:\n")
            print(file.read(20))

            # Moving back to the beginning of the file
            file.seek(0)
            print("\nAfter seek to beginning, reading first line:\n")
            print(file.readline())
    except FileNotFoundError:
        print(f"{filename} not found.\n")


# Demonstrating error handling in file handling
def delete_file(filename):
    try:
        os.remove(f"library_data/{filename}")
        print(f"{filename} deleted successfully.\n")
    except FileNotFoundError:
        print(f"{filename} does not exist, nothing to delete.\n")


# Using file modification and access timestamps
def file_timestamps(filename):
    try:
        stats = os.stat(f"library_data/{filename}")
        print(f"Last access time for {filename}: {datetime.fromtimestamp(stats.st_atime)}")
        print(f"Last modification time for {filename}: {datetime.fromtimestamp(stats.st_mtime)}\n")
    except FileNotFoundError:
        print(f"{filename} not found.\n")


# Execute the functions to demonstrate usage
write_text_file("books.txt", books)
read_text_file("books.txt")

append_text_file("books.txt", [{"title": "Pride and Prejudice", "author": "Jane Austen", "year": 1813}])
read_text_file("books.txt")

write_json_file("books.json", books)
read_json_file("books.json")

write_csv_file("books.csv", books)
read_csv_file("books.csv")

write_pickle_file("books.pkl", books)
read_pickle_file("books.pkl")

demonstrate_seek("books.txt")

file_timestamps("books.txt")
delete_file("books.txt")
delete_file("books.json")
delete_file("books.csv")
delete_file("books.pkl")
