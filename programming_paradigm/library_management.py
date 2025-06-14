class Book:
    def __init__(self, title, author):
        
        self.title = title  
        self.author = author  
        self._is_checked_out = False

    def check_out(self):
        
        if not self._is_checked_out:
            self._is_checked_out = True
            return f'"{self.title}" has been checked out.'
        return f'"{self.title}" is already checked out.'

    def return_book(self):
        
        if self._is_checked_out:
            self._is_checked_out = False
            return f'"{self.title}" has been returned.'
        return f'"{self.title}" was not checked out.'

    def is_available(self):
        
        return not self._is_checked_out

class Library:
    def __init__(self):
        self._books = []
    def add_book(self, book):
        self._books.append(book)
    def check_out_book(self,title):
        for book in self._books:
            if book.title == title and not book._is_checked_out:
                book._is_checked_out = True
                return book.title
        return None
    def return_book(self, title):
        for book in self._books:
            if book.title == title and book._is_checked_out:
                book._is_checked_out = False
                return book.title
        return None
    def list_available_books(self):
            for book in self._books:
                if not book._is_checked_out:
                    print(book.title + " by " + book.author)
            return None
def main():
    # Setup a small library
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

if __name__ == "__main__":
    main()                    