from flask import Flask, request, jsonify, render_template

books = [
    {"id": 1, "title": "Harry Potter","author":"JK Rowling", "year": 1997},
    {"id": 2, "title": "The Great Gatsby","author":"Fitzgerald", "year": 1925},
    {"id": 3, "title": "1984","author":"Orwell", "year": 1949},
    {"id": 4, "title": "To Kill a Mockingbird","author":"Harper Lee", "year": 1960},
]

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '').lower()
    if not query:
        return "No query provided.", 400

    results = [book for book in books if query in book['author'].lower() or query in book['title'].lower()]
    return render_template("results.html", query=query, results=results)

@app.route('/add', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form.get('title')
        author = request.form.get('author')
        year = request.form.get('year')

        if not title or not author or not year:
            return "All fields are required.", 400

        try:
            year = int(year)
        except ValueError:
            return "Year must be a number.", 400

        new_book = {
            "id": len(books) + 1,
            "title": title,
            "author": author,
            "year": year
        }
        books.append(new_book)
        return render_template("add_success.html", book=new_book)

    return render_template("add_book.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
