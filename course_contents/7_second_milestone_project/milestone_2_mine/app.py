from utils import database

USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit

Your choice: """


def prompt_add_book():
    name = input("Name of the book:")
    author = input("Author of the book:")

    database.add_book(name, author)


def list_books():
    books = database.get_all_books()

    if len(books) == 0:
        print("No books, feel free to add some :-)")
        return

    for book_id, book in enumerate(books):
        print_book(book_id, book)


def print_book(book_id, book):
    # print(f"-----------------------------")
    # print(f"Id: {book_id}")
    # print(f"Name: {book['name']}")
    # print(f"Author: {book['author']}")
    # print(f"Book was read: {book['read']}")
    # print(f"-----------------------------")
    read = 'YES' if book['read'] else 'NO'
    print(f"[{book_id}] {book['name']}, {book['author']}, read: {read}")


def prompt_read_book():
    book_id = int(input("Book ID:").strip())
    book = database.mark_book_as_read(book_id)
    if book['read']:
        print("Book marked as read")
    else:
        print("Book marked as unread")

    print_book(book_id, book)


def prompt_delete_book():
    book_id = int(input("Book ID:").strip())
    book = database.delete_book(book_id)

    print_book(book_id, book)


user_options = {
    "a": prompt_add_book,
    "l": list_books,
    "r": prompt_read_book,
    "d": prompt_delete_book
}


def menu():
    user_input = input(USER_CHOICE).lower()
    while user_input != 'q':
        if user_input in user_options:
            selected_function = user_options[user_input]
            selected_function()
        else:
            print('Unknown command. Please try again.')

        user_input = input(USER_CHOICE)


menu()
