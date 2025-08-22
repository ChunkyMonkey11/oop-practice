"""
Design a simple system where users can borrow and return books from a library. Each book can only be borrowed by one user at a time.

Hints

Classes:

Book → title, author, is_borrowed

User → name, borrowed_books

Library → collection of books, methods to borrow/return

Methods:

Library.borrow_book(user, book)

Library.return_book(user, book)

Relationships:

A User has many Books.

A Book belongs to at most one User.

Stretch goals

Add due dates.

Charge late fees.

"""

class Book():
    def __init__(self, book_name, author) -> None:
        self.book_name = book_name
        self.author = author
        self.borrowed = False
        self.current_borrower = None # Assume any book added to the library will have no owner when first intialized. 
        

    def __str__(self):
        return f"The Book name is :{self.book_name}  Borrowed? :{self.borrowed} , Current borrower : {self.current_borrower} "

    def get_book_name(self):
        return self.book_name
    
    def get_book_status(self):
        return self.borrowed
    
    def update_book_status(self, status, user_name):
        self.current_borrower = user_name
        self.borrowed = status

    
class User():
    def __init__(self, user_name, borrowed_books) -> None:
        self.user_name = user_name
        self.borrowed_books = [] # assume the user when first made has 0 books to their name.
    
    def __str__(self) -> str:
        return f"User Name : {self.user_name} || Borrowed Books {self.borrowed_books}"

    def get_user_name(self):
        return self.user_name

    def add_book_to_collection(self, book_name):
        self.borrowed_books.append(book_name)

    def remove_from_borrowed_books(self,book_name):
        self.borrowed_books.remove(book_name)
    


class Library():
    def __init__(self) -> None:
        self.books = {} #Intialize to an empty dict (key: book, value: borrowed)

    def add_book(self, book_name, author):
        if book_name in self.books:
            return "Book already exists in collection"
        self.books[book_name] = Book(book_name, author)
        return "Added!"
    
    def borrow_book(self,book_name, user): #Assume when this is called a user object will be passed in. 
        user_borrowing = user
        if book_name in self.books:
            book = self.books[book_name]

            # check if that book is being borrowed by someone.
            if book.get_book_status() == True:
                return f"Book unavailable someone else is borrowing it"
            else:
                book.update_book_status(True, user.get_user_name())
                user.add_book_to_collection(book.get_book_name())
        else:
            return f"{book_name} is not in our library"

    def return_book(self, book_name, user):
        if book_name not in self.books:
            return f"Book {book_name} is not part of our collection"
        book = self.books[book_name]
        if not book.get_book_status():
            return "Book is not currently borrowed"
        if book.current_borrower != user.get_user_name():
            return "Only the current borrower can return this book"
        book.update_book_status(False, None)
        if book_name in user.borrowed_books:
            user.remove_from_borrowed_books(book_name)
        return "Returned!"
     

