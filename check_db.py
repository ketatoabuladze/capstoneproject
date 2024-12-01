import sqlite3

conn = sqlite3.connect('best_books.db')
cursor = conn.cursor()
cursor.execute('SELECT * FROM book')
rows = cursor.fetchall()
for row in rows:
    print(row)
conn.close()
