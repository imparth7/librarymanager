# Library Manager

This is a simple library management system implemented in Python3 using SQLite3 for data storage. It provides a command-line interface (CLI) for managing books in a library.

## Features

- Add new books to the library.
- List all books available in the library.
- Search for books by title.
- Update book details (title, author, genre, quantity).
- Delete books from the library.

## Requirements

- Python 3.x
- SQLite3

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/imparth7/librarymanager.git
    ```

2. Navigate to the project directory:

    ```bash
    cd librarymanager
    ```

## Usage

1. Run the main script:

    ```bash
    python main.py
    ```

2. Follow the on-screen instructions to perform various operations like adding, listing, searching, updating, or deleting books.

## Database

The library management system uses a SQLite database (`library.db`) to store book information. The database schema includes the following fields:

- `id`: Integer (Primary Key)
- `title`: Text
- `author`: Text
- `genre`: Text
- `quantity`: Integer

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please fork the repository and submit a pull request.