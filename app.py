from flask import Flask, jsonify, request, redirect, render_template, url_for

app = Flask(__name__)

books = [
    {"id": 1, "title": "Мидълмарч", "author": "Джордж Елиът"},
    {"id": 2, "title": "1984", "author": "Джордж Оруел"}
]


@app.route('/')
def home():
    return "Welcome to Flask Book App"


@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)


# @app.route('/books', methods=['POST'])
# def add_book():
#     new_book = request.get_json()
#     if not new_book or 'id' not in new_book or 'title' not in new_book or 'author' not in new_book:
#         return jsonify({"error": "Invalid data"}), 400
#     books.append(new_book)
#     return jsonify(new_book), 201


@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    updated_data = request.get_json()
    for book in books:
        if book['id'] == book_id:
            book.update(updated_data)
            return jsonify(book), 200
    return jsonify({"error": "Book not found"}), 404


@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    for book in books:
        if book['id'] == book_id:
            books.remove(book)
            return jsonify({"message": "Book deleted"}), 200
    return jsonify({"error": "Book not found"}), 404


@app.route('/add', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        new_id = len(books) + 1
        books.append({"id": new_id, "title": title, "author": author})
        return redirect(url_for('home'))  # След добавянето, пренасочва към началната страница
    return render_template('add.html')


if __name__ == '__main__':
    app.run(debug=True)
