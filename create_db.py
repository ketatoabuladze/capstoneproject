import sqlite3

# Connect to the database (creates the file if it doesn't exist)
conn = sqlite3.connect('best_books.db')

# Create a cursor object
cursor = conn.cursor()

# Create the book table
cursor.execute('''
CREATE TABLE IF NOT EXISTS book (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    published_year INTEGER
)
''')

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database 'best_books.db' created with the 'book' table.")

