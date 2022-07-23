from flask import render_template, request, redirect
from app import app
from models.books import books, add_new_book, delete_book
from models.book import Book

@app.route('/books')
def index():
    return render_template('index.html', title='library', books=books)

@app.route('/books/<index>')
def singlebook(index):
  chosenbook = books[int(index)]
  
  return render_template('book.html', book=chosenbook)

@app.route('/books/new')
def new():
    return render_template('new.html', title='New', books=books)

@app.route('/addbook', methods=['POST'])
def addbook():
    bookTitle = request.form['title']
    bookAuthor = request.form['author']
    bookGenre = request.form['genre']
    newBook = Book(title=bookTitle, author=bookAuthor, genre=bookGenre)
    add_new_book(newBook)
    return redirect('/books')

@app.route('/books/delete/<name>', methods=['POST'])
def delete(name):
    delete_book(name)
    return redirect('/books')

