"""
Scope of this project is to understand the
1. Data validation at post request
2. Exception handling
"""
from typing import Optional
from fastapi import FastAPI , Body
from pydantic import BaseModel, Field


app = FastAPI()

class Book:
    """
    A simple book model/class to create record with fields for id, title, author, description, rating, and published_date.
    """
    id: int
    title: str
    author: str
    description: str
    rating: int
    published_date: int

    def __init__(self, id, title, author, description, rating, published_date):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date = published_date


class BookRequest(BaseModel):
    """
    A class to validate the request body for creating a new book.
    """
    id: Optional[int] = Field(description='ID is not needed on create', default=None)
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=0, lt=6)
    published_date: int = Field(gt=1999, lt=2031)

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "A new book",
                "author": "codingwithroby",
                "description": "A new description of a book",
                "rating": 5,
                'published_date': 2029
            }
        }
    }

"""
gt = greater_than
lt = less_than
"""


BOOKS = [
    Book(1, 'Computer Science Pro', 'codingwithroby', 'A very nice book!', 5, 2030),
    Book(2, 'Be Fast with FastAPI', 'codingwithroby', 'A great book!', 5, 2030),
    Book(3, 'Master Endpoints', 'codingwithroby', 'A awesome book!', 5, 2029),
    Book(4, 'HP1', 'Author 1', 'Book Description', 2, 2028),
    Book(5, 'HP2', 'Author 2', 'Book Description', 3, 2027),
    Book(6, 'HP3', 'Author 3', 'Book Description', 1, 2026)
]




@app.get("/books")
async def get_all_books():
    return BOOKS


@app.get("/books/{book_id}")
async def read_book(book_id: int):
    for book in BOOKS:
        if book.id == book_id:
            return book
        

@app.get("/books/", )
async def read_book_by_rating(book_rating: int):
    books_to_return = []
    for book in BOOKS:
        if book.rating == book_rating:
            books_to_return.append(book)
    return books_to_return



"""
Now on create book request we will implement Data Validation.

"""

@app.post("/create-books")
async def create_books(book_request:BookRequest):
    try:
        new_book = Book(**book_request.model_dump())
        BOOKS.append(find_book_id(new_book))
        return {"message": f"Book created successfully."}
    except Exception as e:
        return {"error": str(e)}

def find_book_id(book: Book):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return book


@app.put("/books/update_book")
async def update_book(book: BookRequest):
    book_changed = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i] = book
    
    return {"message": f"Book updated successfully."}


@app.delete("/books/{book_id}")
async def delete_book(book_id: int ):
    book_changed = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            book_changed = True
            break
    if book_changed:
        return {"message": f"Book deleted successfully."}

