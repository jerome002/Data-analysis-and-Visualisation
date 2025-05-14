
from book import Book  # Ensure the file is named 'book.py' (case-sensitive)

class Library:
    def __init__(self):
        self.books = []
        self.current_book = None

    def add_book(self, book):
        self.books.append(book)
    def get_all_books(self):
        for book in self.books:
            print(book.title)
    def get_book_by_id(self, book_id):
        for book in self.books:
            if book.id == book_id:
                return book
        return None
    def update_book(self, book_id, title=None, author=None, year=None):
        book = self.get_book_by_id(book_id)
        if book:
            if title:
                book.title = title
            if author:
                book.author = author
            if year:
                book.year = year
            return True
        return False
    def delete_book(self, book_id):
        book = self.get_book_by_id(book_id)
        if book:
            self.books.remove(book)
            return True
        return False