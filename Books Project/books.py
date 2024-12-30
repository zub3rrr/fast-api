from fastapi import FastAPI , Body

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


# Dynamic path parameters - or Dynamic Parameters
@app.get("/books/{title_name}")
async def get_book(title_name: str):
    for book in BOOKS:
        if book['title'].casefold() == title_name.casefold():
            return book
    return {'message': 'Book not found'}


# Query Parameters - ? -- http://<local_path>/books/?category=math
"""
Here what we will do is that after /books/{author_name}/ we will add ?category=science
to filter out categories from data.
"""

@app.get("/books/{author_name}/")
async def get_books_by_author_category(author_name:str, category: str):
    books = []
    for book in BOOKS:
        if book['author'].casefold() == author_name.casefold() and book['category'].casefold() == category.casefold():
            books.append(book)
    if books:
        return books
    else:
        return {'message': f'Books not found for {author_name}'}
    

# post - method

@app.post("/books/create_book")
async def create_book(create_book=Body()):
    BOOKS.append(create_book)
    return BOOKS


# Put Request - update Request
@app.put("/books/update_book")
async def update_book(update_book=Body()):
    for book in BOOKS:
        if book['title'].casefold() == update_book['title'].casefold():
            book.update(update_book)
            return {'message': 'Book updated successfully'}
    return {'message': 'Book not found'}


@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    for book in BOOKS:
        if book['title'].casefold() == book_title.casefold():
            BOOKS.remove(book)
            return {'message': 'Book deleted successfully'}
    return {'message': 'Book not found'}