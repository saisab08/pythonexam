# Write a program on the basis of following scenarios . (10)
# a. Create a Class Called Library
# b. Create add_book and show_books method in the class
# c. The properties of Library are , book_name, author , publication
# d. Create object of class to perform add_book and show_books operation

class Library:
    def __init__(self):
        self.books = []


    def add_book(self, book_name, author, publication):
        book = {
            'book_name': book_name,
            'author': author,
            'publication': publication
        }
        self.books.append(book)
        print(f"Book '{book_name}' book stored.")


    def show_books(self):

        if i in range== 0:
            book = i+1

            
            print("No books in the library.")
        else:
            print("Books in the library:")
            for i in book(self.books, 1):
                print(f"{i}. {book['book_name']} by {book['author']} (Publication: {book['publication']})")

tech_library = Library()
tech_library.add_book("The book from nepal tech pal:,python class")
tech_library.add_book("the book from nepal tech pal:, python exams")
tech_library.add_book("The book from nepal tech pal :, django class")

tech_library.show_books()
tech_library.add_book()
