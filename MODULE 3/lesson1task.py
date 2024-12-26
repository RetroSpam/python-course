class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}')"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        return self
    
    def remove_book(self, title):
        self.books = [book for book in self.books if book.title != title]
        return self
    
    def __getitem__(self, index):
        return self.books[index]

    def __contains__(self, title):
        return any(book.title == title for book in self.books)

    def __repr__(self):
        return f"Library({self.books})"



library = Library()
library.add_book(Book("1984", "George Orwell")).add_book(Book("Brave New World", "Aldous Huxley"))
print(library)

library.remove_book("1984")
print(library)

print(library[0])

print("1984" in library)
print("Brave New World" in library)