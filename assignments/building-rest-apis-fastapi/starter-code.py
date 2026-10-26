from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Book Library API")


class BookInput(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    author: str = Field(min_length=1, max_length=80)


class Book(BookInput):
    id: int


books = [
    Book(id=1, title="The Hobbit", author="J.R.R. Tolkien"),
    Book(id=2, title="Pride and Prejudice", author="Jane Austen"),
]
next_book_id = 3


@app.get("/health")
def health_check():
    return {"status": "ok"}


# Implement the book routes described in the assignment.
