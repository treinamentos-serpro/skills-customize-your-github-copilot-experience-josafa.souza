# 📘 Assignment: SQLite Persistence with FastAPI

## 🎯 Objective

Extend a FastAPI library API to store books in an SQLite database instead of keeping them only in memory. Practice creating a table, executing SQL queries from Python, and preserving data between server restarts.

## 📝 Tasks

### 🛠️ Create the Database and Books Table

#### Description
Use Python's built-in `sqlite3` module to create a local database for the library. Define a `books` table and initialize it when the API starts.

#### Requirements
The completed program must:

- Use the built-in `sqlite3` module; no separate database server is required.
- Create a database file named `library.db` beside `main.py`.
- Create a `books` table with an integer primary key, a required title, and a required author.
- Initialize the table automatically when the FastAPI application starts.
- Keep the existing `BookInput` validation for titles and authors.

### 🛠️ Implement Database-Backed Book Operations

#### Description
Replace the placeholder API responses with SQL operations so the library API reads and writes books in SQLite.

#### Requirements
The completed program must:

- Return all saved books from `GET /books`.
- Return one book from `GET /books/{book_id}`, or `404 Not Found` if it does not exist.
- Save a book using `POST /books` and return `201 Created` with its assigned ID.
- Update a saved book using `PUT /books/{book_id}`, or return `404 Not Found` if it does not exist.
- Delete a saved book using `DELETE /books/{book_id}`, or return `404 Not Found` if it does not exist.
- Pass SQL values as query parameters rather than building SQL statements by joining user input.

### 🛠️ Verify Persistence and API Responses

#### Description
Run the API and use its interactive documentation to check that the database-backed routes behave correctly and that saved books remain available after a restart.

#### Requirements
The completed program must:

- Rename the downloaded `starter-code.py` to `main.py`, then start the API with `uvicorn main:app --reload` and open the interactive documentation at `/docs`.
- Create a book, retrieve it, update it, and delete it through `/docs`.
- Verify that requesting a missing book returns `404 Not Found`.
- Create a book, restart the server, and verify that the book is still available.
- Confirm that invalid titles or authors are rejected by request validation.
