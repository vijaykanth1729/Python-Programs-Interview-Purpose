# class Library, # available books, lend a book, add a book
# class Customer, # request a book, return a book
class Library:
    def __init__(self, listofbooks):
        self.availableBooks = listofbooks

    def displayAvailableBooks(self):
        print()
        print("Available Books:---> ")
        for book in self.availableBooks:
            print(book)

    def lendBook(self, requestedbook):
        if requestedbook in self.availableBooks:
            print("You have now barrowed the book: ")
            self.availableBooks.remove(requestedbook)
        else:
            print("Sorry your requested Book not available in the library")

    def addBook(self, returnedbook):
        if returnedbook in self.availableBooks:
            print("This book already available in library...check what you barrowed?")
            print()
        else:
            self.availableBooks.append(returnedbook)
            print("Thank you for returning the book..")

class Customer:
    def requestBook(self):
        print("Enter a book you would like to barrow: ")
        self.book = input()
        return self.book

    def returnBook(self):
        print("Enter the name of a book which your returning: ")
        self.book = input()
        return self.book

library = Library(["Think and grow rich", "Napolean hills", "Rich Dad Poor Dad"])
customer = Customer()
while True:
    try:
        print("Enter 1 to display available books:")
        print("Enter 2 to request a book:")
        print("Enter 3 to return a book:")
        print("Enter 4 to Quit:")
        choice = int(input())
        if choice == 1:
            library.displayAvailableBooks()
        elif choice == 2:
            requestBook = customer.requestBook()
            library.lendBook(requestBook)
        elif choice == 3:
            returnedbook = customer.returnBook()
            library.addBook(returnedbook)
        elif choice == 4:
            break
        else:
            print("invalid option, Please choose from the avilable options..")
            print()

    except ValueError:
        print("You enetered invalid option.")
        print()
        continue

    except:
        quit()
