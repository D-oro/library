from flask import render_template, request, redirect
from app import app
from models.orders import orders, add_new_book, delete_book
from models.order import Order

@app.route('/orders')
def index():
    return render_template('index.html', title='Jabba the Pizza Hutt', orders=orders)

@app.route('/orders/<index>')
def singlebook(index):
  chosenbook = orders[int(index)]
  
  return render_template('order.html', order=chosenbook)

@app.route('/order/new')
def new():
    return render_template('new.html', title='New', orders=orders)

@app.route('/addbook', methods=['POST'])
def addbook():
    bookTitle = request.form['title']
    bookAuthor = request.form['author']
    bookGenre = request.form['genre']
    newBook = Order(title=bookTitle, author=bookAuthor, genre=bookGenre)
    add_new_book(newBook)
    return redirect('/orders')

@app.route('/orders/delete/<name>', methods=['POST'])
def delete(name):
    delete_book(name)
    return redirect('/orders')

