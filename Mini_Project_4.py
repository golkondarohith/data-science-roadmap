#Library Managemnet System
class Library():
    def __init__(self, book_title, book_author, available_copies):
        self.book_title = book_title
        self.book_author = book_author
        self.available_copies = available_copies

#Adding a book
def add_book():
        available_copies = 0
        book_title = input("Enter the book title: ")
        book_author = input("Enter the book author name: ")
        for book, author in books:
            if book == "book_title" and author == "book_author":
                available_copies += 1
        books.append(Library(book_title, book_author, available_copies))
        print("Book added to library successfully....")


#Main program
books = []


#Writing into the file
with open("library_records.txt", "a") as f:
     for book in books:
          f.write(f"Book {book.book_title} wwritten by {book.book_author} and available copies {book.available_copies}")




add_book()

#Printing the books
for book in books:
    print(f"Book {book.book_title} written by {book.book_author}and available copies {book.available_copies}")