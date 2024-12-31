books = []

def add_book(book):
    books.append(book)
    print(f'"{book}" added to the library.')

def borrow_book(book_name):
    """Borrow a book from the library."""
    if book_name in books:
        books.remove(book_name)
        print(f'You have borrowed "{book_name}".')
    else:
        print(f'Sorry, "{book_name}" is not available in the library.')

def return_book(book):
    books.append(book)
    print(f'"{book}" returned to the library.')

def display_books():
    if books:
        print("Available books in the library:")
        for book in books:
            print(f"- {book}")
    else:
        print("No books are currently available in the library.")

def search_book():
    if books:
        search_term = input("Enter the name of the book to search: ")
        matching_books = [book for book in books if search_term.lower() in book.lower()]
        if matching_books:
            print("Matching books:")
            for book in matching_books:
                print(f"- {book}")
        else:
            print(f'No books found matching "{search_term}".')
    else:
        print("The library is empty. No books to search.")

# User input loop
while True:
    
    print("\nChoose an option")
    print("1.  Add a Book ")
    print("2.  Borrow a Book")
    print("3. Return a Book")
    print("4. Show Available Books")
    print("5. Search for a Book")    
    print("6. Exit")
    user_input = input("Enter choice (1/2/3/4/5/6): ")
    if user_input == '1':
        book = input("Enter the name of the book to add: ")
        add_book(book)

    elif user_input == '2':
        book = input("Enter the name of the book to borrow: ")
        borrow_book(book)

    elif user_input == '3':
        book = input("Enter the name of the book to return: ")
        return_book(book)

    elif user_input == '4':
        display_books()

    elif user_input == '5':
        search_book()  

    elif user_input == '6':
        print("Exiting the system. Have a nice day!")
        break

    else:
        print("Invalid option. Please try again.")
