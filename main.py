# Python
import names
import random

# Flask
from flask import (
    Flask,
    request,
    Request,
    Response,
    render_template,
)
from flask.app import Flask as FlaskApp

# Local
from models.book import Book


app: FlaskApp = Flask(__name__)
books: list[Book] = []

@app.route('/')
def main_page():
    return render_template(
        template_name_or_list="index.html",
        ctx_books=enumerate(books)
    )

@app.route('/search', methods=['GET', 'POST'])
def search_books():
    find_data: str = "Песнь огня"
    result: list[Book] = []
    for book in books:
        if find_data.lower() in book.title.lower():
            result.append(book)

    if len(result) <= 0:
        return "Book not found!"

    return render_template(
        template_name_or_list="index.html",
        ctx_books=enumerate(result)
    )

@app.route('/<id>')
def current_book(id: str):
    try:
        return render_template(
            template_name_or_list="book.html",
            ctx_book=books[int(id)]
        )
    except:
        return "Произошла ошибка"

@app.route('/create', methods=['GET', 'POST'])
def create_book():
    result: list[Book] = []
    if request.method == "POST":
        book = Book(
                title=request.form.get('title'),
                description=request.form.get('description'),
                price=request.form.get('price'),
                list_count=request.form.get('list_count'),
                rate_list=[
                    int(i)
                    for i in request.form.get("rate")
                ]
            )
        books.append(book)
        result.append(book)
        
    return render_template(
        template_name_or_list="create.html",
        ctx_books=enumerate(result)
    )
    


if __name__ == '__main__':
    _: int
    for _ in range(1000):
        book = Book(
            title=names.get_first_name(),
            description=names.get_last_name(),
            price=round(
                random.random() * 500 + 500,
                2
            ),
            list_count=random.randint(100, 600),
            rate_list=[
                random.randint(1, 10) 
                for _ in range(random.randint(1, 60))
            ]
        )
        books.append(book)

    app.run(
        host='localhost',
        port=8080,
        debug=True
    )