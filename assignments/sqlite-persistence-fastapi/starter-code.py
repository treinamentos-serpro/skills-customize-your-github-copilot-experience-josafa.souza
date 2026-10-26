import sqlite3
from pathlib import Path

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

DATABASE_PATH = Path(__file__).with_name("library.db")

app = FastAPI(title="SQLite Library API")


class BookInput(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    author: str = Field(min_length=1, max_length=80)


class Book(BookInput):
    id: int


def get_connection() -> sqlite3.Connection:
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database() -> None:
    with get_connection() as connection:
        # TODO: Create the books table if it does not exist.
        pass


@app.on_event("startup")
def on_startup() -> None:
    initialize_database()


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/books", response_model=list[Book])
def list_books() -> list[Book]:
    # TODO: Query the database and return all books.
    raise HTTPException(status_code=501, detail="Implement book listing")


@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int) -> Book:
    # TODO: Query by ID and return 404 when the book does not exist.
    raise HTTPException(status_code=501, detail="Implement book lookup")


@app.post("/books", response_model=Book, status_code=201)
def create_book(book_input: BookInput) -> Book:
    # TODO: Insert the book and return it with its new database ID.
    raise HTTPException(status_code=501, detail="Implement book creation")


@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, book_input: BookInput) -> Book:
    # TODO: Update the book and return 404 when the ID does not exist.
    raise HTTPException(status_code=501, detail="Implement book update")


@app.delete("/books/{book_id}", status_code=204)
def delete_book(book_id: int) -> None:
    # TODO: Delete the book and return 404 when the ID does not exist.
    raise HTTPException(status_code=501, detail="Implement book deletion")
