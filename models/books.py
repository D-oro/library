from models.book import *

book1 = Book("Talk to your duck - an introduction to coding", "Ducky McDuck", "How-to guides")
book2 = Book("The Mousetrap", "Kat Kitten", "Mystery")
book3 = Book("The Chicken or the Egg", "Hen Rooster", "Biography")
books = [book1, book2, book3]

def add_new_book(book):
    books.append(book)

def delete_book(book_name):
    book_to_delete = None
    for book in books:
        if book.title == book_name:
            event_to_delete = book
            break

    books.remove(event_to_delete)