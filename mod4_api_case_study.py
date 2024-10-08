from crypt import methods

from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)


def get_db():
    conn = sqlite3.connect('books.db')
    return conn


@app.route('/books', methods=['GET'])
def get_books():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM books')
    books = cursor.fetchall()
    conn.close()
    return jsonify(books)


@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM books WHERE id = ?', (book_id))
    book = cursor.fetchone()
    conn.close()
    if book:
        return jsonify()
    return jsonify({'error': 'Book not ofund'}), 404


@app.route('/books', methods=['POST'])
def add_book():
    new_book = request.get_json()
    book_name = new_book['book_name']
    author = new_book['author']
    publisher = new_book['publisher']
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO books (book_name, author, publisher) VALUES (?, ?, ?)', (book_name, author, publisher))

    conn.commit()
    conn.close()
    return jsonify(new_book), 201


@app.route('/books/<int:back_id>', methods=['PUT'])
def update_book(book_id):
    updated_book = request.get_json()
    book_name = updated_book['book_name']
    author = updated_book['author']
    publisher = updated_book['publisher']
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('UPDATE books SET book_name = ?, author = ?, publisher = ? WHERE id = ?',
                   (book_name, author, publisher, book_id))

    conn.commit()
    conn.close()
    return jsonify(updated_book)


@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM books WHERE id = ?', (book_id), )
    conn.commit()
    conn.close()
    return jsonify({'Message': 'Book deleted'})


if __name__ == '__main__':
    app.run(debug=True)
