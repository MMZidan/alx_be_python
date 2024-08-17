

class Book:
    def __init__(self,title:str,author:str):
        self.title=title
        self.author=author
        self._is_checked_out = False 

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

    def __str__(self):
        """Return a string representation of the book."""
        return f'{self.title} by {self.author}'


class Library:
    def __init__(self):
        self._books = []

    def add_book(self,book):
            self._books.append(book)
    
    def list_available_books(self):
        for i in self._books:
            if i._is_checked_out == False:
                print(i)
            pass           
    def check_out_book(self,title):
        for i in self._books:
            if i.title== title:
                if i.is_available()==True:
                    i.check_out()
            
    def return_book(self,title):
        for i in self._books:
            if i.title==title:
                i.return_book()
