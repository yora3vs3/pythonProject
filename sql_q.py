import sqlite3
from datetime import datetime

# Connect to an in-memory SQLite database
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

# Enable foreign key constraints
conn.execute("PRAGMA foreign_keys = 1")

# Create tables for a library management system
cursor.execute('''CREATE TABLE Authors (
                    author_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    birth_year INTEGER
                )''')

cursor.execute('''CREATE TABLE Genres (
                    genre_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL UNIQUE
                )''')

cursor.execute('''CREATE TABLE Books (
                    book_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    author_id INTEGER,
                    genre_id INTEGER,
                    year_published INTEGER,
                    available INTEGER DEFAULT 1,
                    FOREIGN KEY(author_id) REFERENCES Authors(author_id),
                    FOREIGN KEY(genre_id) REFERENCES Genres(genre_id)
                )''')

cursor.execute('''CREATE TABLE Borrowers (
                    borrower_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    membership_start DATE
                )''')

cursor.execute('''CREATE TABLE BorrowedBooks (
                    borrow_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    book_id INTEGER,
                    borrower_id INTEGER,
                    borrow_date DATE,
                    return_date DATE,
                    FOREIGN KEY(book_id) REFERENCES Books(book_id),
                    FOREIGN KEY(borrower_id) REFERENCES Borrowers(borrower_id)
                )''')

# Commit the table creation
conn.commit()

# Inserting sample data with transaction management and error handling
try:
    with conn:
        # Insert genres
        genres = ['Fiction', 'Non-fiction', 'Science Fiction', 'Fantasy']
        for genre in genres:
            cursor.execute("INSERT INTO Genres (name) VALUES (?)", (genre,))

        # Insert authors
        authors = [('Isaac Asimov', 1920), ('George Orwell', 1903), ('J.K. Rowling', 1965)]
        cursor.executemany("INSERT INTO Authors (name, birth_year) VALUES (?, ?)", authors)

        # Insert books
        books = [
            ('1984', 2, 1, 1949),  # George Orwell, Fiction
            ('Foundation', 1, 3, 1951),  # Isaac Asimov, Science Fiction
            ('Harry Potter and the Sorcerer\'s Stone', 3, 4, 1997)  # J.K. Rowling, Fantasy
        ]
        cursor.executemany("INSERT INTO Books (title, author_id, genre_id, year_published) VALUES (?, ?, ?, ?)", books)

        # Insert borrowers
        borrowers = [('Alice Johnson', '2023-01-01'), ('Bob Smith', '2022-05-15')]
        cursor.executemany("INSERT INTO Borrowers (name, membership_start) VALUES (?, ?)", borrowers)

except sqlite3.Error as e:
    print("An error occurred:", e)


# Sample transaction: Borrow a book
def borrow_book(book_id, borrower_id):
    try:
        with conn:
            # Check if the book is available
            cursor.execute("SELECT available FROM Books WHERE book_id = ?", (book_id,))
            result = cursor.fetchone()
            if not result or result[0] == 0:
                raise Exception("Book is not available for borrowing.")

            # Borrow the book (update availability and create a record)
            borrow_date = datetime.now().strftime('%Y-%m-%d')
            cursor.execute("INSERT INTO BorrowedBooks (book_id, borrower_id, borrow_date) VALUES (?, ?, ?)",
                           (book_id, borrower_id, borrow_date))
            cursor.execute("UPDATE Books SET available = 0 WHERE book_id = ?", (book_id,))

            print(f"Book with ID {book_id} successfully borrowed by borrower ID {borrower_id}.")
    except sqlite3.Error as e:
        print("Database error:", e)
    except Exception as e:
        print("Error:", e)


# Borrow a book
borrow_book(1, 1)  # Alice Johnson borrows "1984"

# Complex query examples
print("\n--- Complex Queries ---\n")

# Query: List all books with author and genre
cursor.execute('''SELECT Books.title, Authors.name AS author, Genres.name AS genre, Books.year_published
                  FROM Books
                  JOIN Authors ON Books.author_id = Authors.author_id
                  JOIN Genres ON Books.genre_id = Genres.genre_id''')
for row in cursor.fetchall():
    print("Book:", row)

# Query: List all borrowed books with borrower details
cursor.execute('''SELECT Books.title, Borrowers.name AS borrower, BorrowedBooks.borrow_date
                  FROM BorrowedBooks
                  JOIN Books ON BorrowedBooks.book_id = Books.book_id
                  JOIN Borrowers ON BorrowedBooks.borrower_id = Borrowers.borrower_id''')
for row in cursor.fetchall():
    print("Borrowed Book:", row)

# Query: Count books by genre
cursor.execute('''SELECT Genres.name, COUNT(Books.book_id) AS total_books
                  FROM Genres
                  LEFT JOIN Books ON Genres.genre_id = Books.genre_id
                  GROUP BY Genres.name''')
for row in cursor.fetchall():
    print("Genre Count:", row)

# Query: Find books that were borrowed by a specific borrower
borrower_name = 'Alice Johnson'
cursor.execute('''SELECT Books.title, BorrowedBooks.borrow_date
                  FROM BorrowedBooks
                  JOIN Books ON BorrowedBooks.book_id = Books.book_id
                  JOIN Borrowers ON BorrowedBooks.borrower_id = Borrowers.borrower_id
                  WHERE Borrowers.name = ?''', (borrower_name,))
for row in cursor.fetchall():
    print(f"Books borrowed by {borrower_name}:", row)

# Close connection
conn.close()
