import json
from flask import Flask, jsonify, request;

app = Flask(__name__)

books = [
    {
        'id': 1,
        'title': 'The Lord of the Rings - Return of The King',
        'writer': 'J.R.R Tolkien'
    },
    {
       'id': 2,
        'title': 'The Hobbit',
        'writer': 'J.R.R Tolkien' 
    },
    {
       'id': 3,
        'title': 'O primeiro milhão',
        'writer': 'Thiago Nigro' 
    }
]


@app.route('/books',methods=['GET'])
def get_books():
    return jsonify(books)

@app.route('/books/<int:id>',methods=['GET'])
def get_books_by_id(id):
    for book in books:
        if book.get('id') == id:
            return jsonify(book)

@app.route('/books/<int:id>',methods=['PUT'])
def edit_book_by_id(id):
    changed_book = request.get_json()
    for index, book in enumerate(books):
        if book.get('id') == id:
            books[index].update(changed_book)
            return jsonify(books[index])

@app.route('/books',methods=['POST'])
def add_new_book():
    new_book = request.get_json()
    books.append(new_book)
    return jsonify(books)

@app.route('/books/<int:id>',methods=['DELETE'])
def delete_book(id):
    for index, book in enumerate(books):
        if book.get('id') == id:
            del books[index]

        return jsonify(books)


app.run(port=5000,host='localhost',debug=True)