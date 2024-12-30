from fastapi import FastAPI

app = FastAPI()

BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
]

@app.get("/books")
async def get_all_books():
    return BOOKS

"""
1. 
%20 means space.


2.
Always dynamic path parameters will be at last 
order of reading API in FastAPI :
                                 Static > Dynamic
"""

@app.get("/books/{title_name}")
async def get_book(title_name: str):
    for book in BOOKS:
        if book['title'].casefold() == title_name.casefold():
            return book
    return {'message': 'Book not found'}