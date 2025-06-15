class Book:
    """ A class representing books in  library. """

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Mark the book as checked out. """
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Mark the book as  returned (Availble)."""
        if self._is_checked_out:
            return True
        return False

    def is_available(self):
        """Return true if the book is available (not checked out)."""
        return not self._is_checked_out


class Library:
    """ class representing a library that manages a collection of books."""

    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return
        print(f"Book '{title}' is not available for checkout.")

    def return_book(self, title):
        """Return book by title to make it avalable again"""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return
        print(f"Book '{title}' was not checked out or does not exist.")

    def list_available_books(self):
        """List all books available."""
        available_books = [book for book in self._books if book.is_available()]
        if not available_books:
            print("No available books.")
        else:
            for book in available_books:
                print(f"{book.title} by {book.author}")
