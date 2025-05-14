
from book import Book
from library import Library

def show_menu():
    print("\n Library Menu:")
    print("1. Add new book")
    print("2. View all books")
    print("3. View a book by ID")
    print("4. Update a book")
    print("5. Delete a book")
    print("6. Exit")

def main():
    library = Library()
    while True:
        show_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            # Add new book
            book_id = input("Enter book ID: ")
            title = input("Enter title: ")
            author = input("Enter author: ")
            year = input("Enter publication year: ")

            book = Book(book_id, title, author, year)
            library.add_book(book)
            print("Book added successfully.")

        elif choice == '2':
            # View all books
            books = library.get_all_books()
            if books:
                print("\n📖 All Books:")
                for b in books:
                    print(b)
            else:
                print("No books found.")

        elif choice == '3':
            # View book by ID
            book_id = input("Enter book ID: ")
            book = library.get_book_by_id(book_id)
            if book:
                print("\n📘 Book Details:")
                print(book)
            else:
                print(" Book not found.")

        elif choice == '4':
            # Update book
            book_id = input("Enter book ID to update: ")
            print("Leave any field blank to keep current value.")
            title = input("New title: ")
            author = input("New author: ")
            year = input("New year: ")

            updated = library.update_book(
                book_id,
                title=title if title else None,
                author=author if author else None,
                year=year if year else None
            )
            if updated:
                print(" Book updated.")
            else:
                print(" Book not found.")

        elif choice == '5':
            # Delete book
            book_id = input("Enter book ID to delete: ")
            deleted = library.delete_book(book_id)
            if deleted:
                print("🗑️ Book deleted.")
            else:
                print(" Book not found.")

        elif choice == '6':
            print("👋 Exiting program. Goodbye!")
            break

        else:
            print(" Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()
