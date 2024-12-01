import sqlite3

conn = sqlite3.connect('best_books.db')
cursor = conn.cursor()

# Insert sample data into the book table
sample_books = [
    ('To Kill a Mockingbird', 'Harper Lee', 1960),
    ('1984', 'George Orwell', 1949),
    ('Pride and Prejudice', 'Jane Austen', 1813)
]

cursor.executemany('INSERT INTO book (title, author, published_year) VALUES (?, ?, ?)', sample_books)

conn.commit()
conn.close()

print("Sample data loaded into 'best_books.db'.")
