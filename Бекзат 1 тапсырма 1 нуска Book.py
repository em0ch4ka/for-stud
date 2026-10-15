class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Кітапханаға қосылды: {book.title}")

    def lend_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f"Оқырманға берілді: {book.title} - {book.author}")
                return
        print("Кітап табылмады!")


book1 = Book("Абай жолы", "Мұхтар Әуезов")
book2 = Book("Қан мен тер", "Әбдіжәміл Нұрпейісов")

library = Library()

library.add_book(book1)
library.add_book(book2)

library.lend_book("Абай жолы")