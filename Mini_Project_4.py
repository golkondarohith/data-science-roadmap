#Library Managemnet System
class Library():
    def __init__(self, book_title, book_author, available_copies = 1):
        self.book_title = book_title
        self.book_author = book_author
        self.available_copies = available_copies


#List to store books
books = []


#Function to add a book
def add_book():
        book_title = input("Enter the book title: ")
        book_author = input("Enter the book author name: ")

        #check if book already exist
        for book in books:
            if book.book_title == book_title and book.author == book_author:
                book.available_copies += 1
                print("Another copy added successfully!")
                return
        #if book doesn't exists, add new
        books.append(Library(book_title, book_author, 1))
        print("Book added to library successfully....")

#Function to save records into file
def save_records():
    with open("library_records.txt", "a") as f:
         for book in books:
            f.write(
                f"Book '{book.book_title}' written by {book.book_author}, "
                f"Available copies: {book.available_copies}\n"
            )


#Main program
add_book()
save_records()





