from models.order import *

book1 = Order("Talk to your duck - an introduction to coding", "Ducky McDuck", "How-to guides")
book2 = Order("The Mousetrap", "Kat Kitten", "Mystery")
book3 = Order("The Chicken or the Egg", "Hen Rooster", "Biography")
orders = [book1, book2, book3]

def add_new_book(order):
    orders.append(order)

def delete_book(book_name):
    book_to_delete = None
    for order in orders:
        if order.title == book_name:
            event_to_delete = order
            break

    orders.remove(event_to_delete)