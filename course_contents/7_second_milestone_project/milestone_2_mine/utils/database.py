"""
Concerned with storing and retrieving books from a list
"""

books = []


def get_all_books():
    return books


def add_book(name, author):
    books.append({'name': name, 'author': author, 'read': False})


def get_book(book_id):
    return books[book_id]


def mark_book_as_read(book_id):
    books[book_id]['read'] = not books[book_id]['read']
    return books[book_id]


def delete_book(book_id):
    book = books.pop(book_id)
    return book

