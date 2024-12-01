const express = require('express');
const mysql = require('mysql2');
const bodyParser = require('body-parser');

const app = express();
app.use(bodyParser.json());

const db = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: 'Ketato2204$', 
    database: 'best_books'
});

db.connect((err) => {
    if (err) throw err;
    console.log('Connected to MySQL database.');
});

app.get('/books', (req, res) => {
    db.query('SELECT * FROM books', (err, results) => {
        if (err) throw err;
        res.json(results);
    });
});

app.post('/add-book', (req, res) => {
    const { title, author, published_year } = req.body;
    const query = 'INSERT INTO books (title, author, published_year) VALUES (?, ?, ?)';
    db.query(query, [title, author, published_year], (err) => {
        if (err) throw err;
        res.json({ message: 'Book added successfully!' });
    });
});

app.put('/update-book/:id', (req, res) => {
    const { title, author, published_year } = req.body;
    const query = 'UPDATE books SET title = ?, author = ?, published_year = ? WHERE id = ?';
    db.query(query, [title, author, published_year, req.params.id], (err) => {
        if (err) throw err;
        res.json({ message: 'Book updated successfully!' });
    });
});

app.delete('/delete-book/:id', (req, res) => {
    const query = 'DELETE FROM books WHERE id = ?';
    db.query(query, [req.params.id], (err) => {
        if (err) throw err;
        res.json({ message: 'Book deleted successfully!' });
    });
});

app.listen(5000, () => {
    console.log('Server is running on port 5000');
});
