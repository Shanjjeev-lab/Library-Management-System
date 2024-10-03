class Library:
    book = []
    def __init__(self,booklist):
        self.books = bookList
    def display(self):
        for i in self.books:
            print(i)

    def borrow(self, book):
        if book in self.books:
            self.books.remove(book)
            print("You have borrowed the book!", book)
        else:
            print("I am Sorry. This book is not available")
            

bookList = ["The Great Bash", "BlueLock", "The War of 1945"]
library = Library(bookList)

while True:
    print("\n--- Library Menu ---")
    print("1. Display Books")
    print("2. Borrow a book")
    print("3. Return a book")
    print("4. Exit")
    choice = input("Enter a choice [1/2/3/4]:")

    if choice == "1":
        library.display()
        
    elif choice == "2":
        book = input("Enter the book you want to borrow: ")
        library.borrow(book)
        
    elif choice == "4":
        break
    else:
         print("Please choose a valid option")
