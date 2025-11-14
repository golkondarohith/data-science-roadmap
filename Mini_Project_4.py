# Library Management System
class Library:
    def __init__(self, book_title, book_author, available_copies=1):
        self.book_title = book_title
        self.book_author = book_author
        self.available_copies = available_copies


# List to store books
books = []


# Function to add a book
def add_book():
    book_title = input("Enter the book title: ").strip()
    book_author = input("Enter the book author name: ").strip()

    # check if book already exists
    for book in books:
        if book.book_title.lower() == book_title.lower() and book.book_author.lower() == book_author.lower():
            book.available_copies += 1
            print("Another copy added successfully!")
            log_action(f"Updated: '{book_title}' by {book_author}, total copies = {book.available_copies}")
            return

    # if book doesn't exist, add new
    books.append(Library(book_title, book_author, 1))
    print("Book added to library successfully....")
    log_action(f"Added new: '{book_title}' by {book_author}, copies = 1")


# Function to log each action
def log_action(action_message):
    with open("library_log.txt", "a") as f:   # separate log file
        f.write(action_message + "\n")


# Function to save snapshot of current state
def save_snapshot():
    with open("library_snapshot.txt", "w") as f:   # overwrite snapshot
        for book in books:
            f.write(
                f"Book '{book.book_title}' written by {book.book_author}, "
                f"Available copies: {book.available_copies}\n"
            )
    print("Snapshot saved to library_snapshot.txt")

# Load snapshot when program starts
def load_snapshot():
    try:
        with open("library_snapshot.txt", "r") as f:
            for line in f:
                parts = line.strip().split(",")
                title = parts[0].split("'")[1]
                author = parts[1].replace(" written by ", "").strip()
                copies = int(parts[2].split(":")[1])
                books.append(Library(title, author, copies))
    except FileNotFoundError:
        pass  # no snapshot yet, start fresh




#Main program
# Main program
load_snapshot()
add_book()
save_snapshot()






