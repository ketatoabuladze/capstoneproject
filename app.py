from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def connect_db():
    try:
        conn = sqlite3.connect('best_books.db')
        return conn
    except sqlite3.Error as e:
        print(f"Database connection error: {e}")
        return None

@app.route('/books', methods=['GET'])
def get_books():
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM book')
        rows = cursor.fetchall()
        books = [{"id": row[0], "title": row[1], "author": row[2], "published_year": row[3]} for row in rows]
        conn.close()
        return jsonify(books)
    else:
        return jsonify({"error": "Database connection failed"}), 500

@app.route('/books', methods=['POST'])
def add_book():
    new_book = request.get_json()
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO book (title, author) VALUES (?, ?)',
                   (new_book['title'], new_book['author']))
    conn.commit()
    conn.close()
    return jsonify(new_book), 201

@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    updated_book = request.get_json()
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('UPDATE book SET title = ?, author = ? WHERE id = ?',
                   (updated_book['title'], updated_book['author'], id))
    conn.commit()
    conn.close()
    return jsonify(updated_book)

@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM book WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)

