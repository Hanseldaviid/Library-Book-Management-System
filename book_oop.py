# Bookstore

class Book:
    def __init__(self, title_book, author, pages, release_year):
        self.title_book = title_book
        self.author = author
        self.pages = pages
        self.release_year = release_year
       
class Library:
    def __init__(self, library_name):
        self.library_name = library_name
        self.books = []
        
    def add_book(self, book):
        self.books.append(book)
    
    def show_catalog(self):
        print(" = = B O O K S = = \n") 
        for b in self.books:
            print(f"Title: {b.title_book} | Author: {b.author} | Pages: {b.pages} | Realease year: {b.release_year}")  
    
    def count_books(self):
        amount = len(self.books)
        print(f"Books in the library: {amount}")
    
    def total_pages(self):
        total = 0
        for b in self.books:
            total += b.pages    
        print(f"Total pages written by Brandon Sanderson: {total}")
    
book1 = Book("The way of kins",       "Brandon Sanderson",    1188,  "2010") 
book2 = Book("The wall of ascention", "Brandon Sanderson",    720,   "2007")
book3 = Book("Radiant words",         "Brandon Sanderson",    1450,  "2014")
book4 = Book("The judgment",          "Brandon Sanderson",    523,    "2017")

my_library = Library("Panamericana Library")

my_library.add_book(book1)  
my_library.add_book(book2) 
my_library.add_book(book3) 
my_library.add_book(book4)

my_library.show_catalog()

my_library.count_books()

my_library.total_pages()



           