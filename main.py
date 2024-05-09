import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('library.db')
cursor = conn.cursor()

# Create books table
cursor.execute('''CREATE TABLE IF NOT EXISTS books (
                    id INTEGER PRIMARY KEY,
                    title TEXT,
                    author TEXT,
                    genre TEXT,
                    quantity INTEGER
                )''')
conn.commit()

# CRUD operations

def add_book(title, author, genre, quantity):
    cursor.execute('''INSERT INTO books (title, author, genre, quantity)
                      VALUES (?, ?, ?, ?)''', (title, author, genre, quantity))
    conn.commit()

def list_books():
    cursor.execute('''SELECT * FROM books''')
    books = cursor.fetchall()
    if not books:
        print("No books available.")
    else:
        print("Books available in the library:")
        for book in books:
            print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Genre: {book[3]}, Quantity: {book[4]}")

def search_book(title):
    cursor.execute('''SELECT * FROM books WHERE title LIKE ?''', (f'%{title}%',))
    books = cursor.fetchall()
    if not books:
        print("Book not found.")
    else:
        print("Search result:")
        for book in books:
            print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Genre: {book[3]}, Quantity: {book[4]}")

def update_book(book_id, title, author, genre, quantity):
    cursor.execute('''UPDATE books SET title=?, author=?, genre=?, quantity=? WHERE id=?''',
                   (title, author, genre, quantity, book_id))
    conn.commit()

def delete_book(book_id):
    cursor.execute('''DELETE FROM books WHERE id=?''', (book_id,))
    conn.commit()

# CLI Interface
def main():
    print("Welcome to the Library Management System!")

    while True:
        print("\n1. Add a book")
        print("2. List all books")
        print("3. Search for a book")
        print("4. Update a book")
        print("5. Delete a book")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter title: ")
            author = input("Enter author: ")
            genre = input("Enter genre: ")
            quantity = int(input("Enter quantity: "))
            add_book(title, author, genre, quantity)
            print("Book added successfully.")
        elif choice == "2":
            list_books()
        elif choice == "3":
            title = input("Enter the title of the book to search: ")
            search_book(title)
        elif choice == "4":
            book_id = int(input("Enter the ID of the book to update: "))
            title = input("Enter new title (press Enter to keep the same): ")
            author = input("Enter new author (press Enter to keep the same): ")
            genre = input("Enter new genre (press Enter to keep the same): ")
            quantity = int(input("Enter new quantity (press Enter to keep the same): "))
            update_book(book_id, title, author, genre, quantity)
            print("Book updated successfully.")
        elif choice == "5":
            book_id = int(input("Enter the ID of the book to delete: "))
            delete_book(book_id)
            print("Book deleted successfully.")
        elif choice == "6":
            print("Thank you for using the Library Management System!")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
