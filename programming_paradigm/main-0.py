class Book:
    def __init__(self, title, author):
        self.title = title  # Public attribute for the book title
        self.author = author  # Public attribute for the book author
        self._is_checked_out = False  # Private attribute to track availability

    def check_out(self):
        """Check out the book if it is available."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Return the book to the library."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Check if the book is available."""
        return not self._is_checked_out


class Library:
    def __init__(self):
        self._books = []  # Private list to store Book instances

    def add_book(self, book):
        """Add a new book to the library."""
        if isinstance(book, Book):
            self._books.append(book)
            print(f'Book "{book.title}" by {book.author} added to the library.')
        else:
            print("Only instances of Book can be added.")

    def check_out_book(self, title):
        """Check out a book by its title."""
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print(f'You have checked out "{book.title}".')
                    return
                else:
                    print(f'Sorry, "{book.title}" is already checked out.')
                    return
        print(f'Sorry, the book "{title}" is not found in the library.')

    def return_book(self, title):
        """Return a checked-out book by its title."""
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f'Thank you for returning "{book.title}".')
                    return
                else:
                    print(f'The book "{book.title}" was not checked out.')
                    return
        print(f'Sorry, the book "{title}" is not found in the library.')

    def list_available_books(self):
        """List all available books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            print("Available books in the library:")
            for book in available_books:
                print(f'- {book.title} by {book.author}')
        else:
            print("No books are currently available in the library.")


# The following code is for testing purposes and should be placed in main.py
if __name__ == "__main__":
    # Create library instance
    library = Library()
    library.add_book(Book("Brave New World", "Aldous Huxley"))
    library.add_book(Book("1984", "George Orwell"))

    # Initial list of available books
    print("Available books after setup:")
    library.list_available_books()

    # Simulate checking out a book
    library.check_out_book("1984")
    print("\nAvailable books after checking out '1984':")
    library.list_available_books()

    # Simulate returning a book
    library.return_book("1984")
    print("\nAvailable books after returning '1984':")
    library.list_available_books()
