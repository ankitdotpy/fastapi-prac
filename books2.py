from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel, Field
from uuid import UUID
from hashlib import sha256
import exceptions as exp

app = FastAPI()

class Book(BaseModel):
    id:UUID
    title:str = Field(
        min_length = 1,
        max_length= 100
    )
    author:str = Field(
        min_length = 1,
        max_length= 100
    )
    description:Optional[str] = Field(
        title= 'Description of the book',
        min_length=1,
        max_length=200
    )
    rating:int = Field(
        ge=0, le=10
    )

Books = {}

@app.get('/')
def read_books(book_to_return:Optional[int] = None):
    if len(Books)<1:
        create_books_no_api()
    if book_to_return and len(Books)>=book_to_return>0:
        return Books[:book_to_return] 
    return Books

@app.get('/book/{book_id}')
def read_books(book_id:UUID):
    key = find_key_256(str(book_id))
    if Books.get(key):
        return Books[key]
    raise exp.item_not_found()

@app.post('/')
def add_book(book:Book):
    Books.append(book)
    return book

@app.post('/{book_id}')
def update_book(book_id:UUID, book:Book):
    key = find_key_256(book_id)
    if Books.get(key):
        Books[key] = book
        return f'Updated book at {key}'
    raise exp.item_not_found()

@app.delete('/{book_id}')
def delete_book(book_id:UUID):
    key = find_key_256(book_id)
    if Books.get(key):
        del Books[key]
        return f'deleted book at {key}'
    raise exp.item_not_found()


def create_books_no_api():
    book1 = Book(
        id = '49a03a48-c699-4395-8a7d-a507a6dd8bbe',
        title='Random Bullshit Go',
        author='Ankit Dhiman',
        description='Some random description',
        rating=10
    )

    book2 = Book(
        id = '49a03a48-c699-4335-8a7d-a507a6dd8bbe',
        title='peepeepoopoo',
        author='Doraemon',
        description='peepeepoopoo description',
        rating=9
    )

    book3 = Book(
        id = '49a03a48-c969-4395-8a7d-a507a6dd8dee',
        title='Super Strikers',
        author='Ching Hang Le',
        description='Book description goes here',
        rating=7
    )

    book4 = Book(
        id = '49c03a48-c699-4395-8a7d-a507a6dd8bbe',
        title='Haryana State',
        author='Ankit Dhiman',
        description='best book on best state of Indian union',
        rating=10
    )

    book5 = Book(
        id = '49a07a48-c699-4395-8a7d-a507a6dd8bbe',
        title='Random Bullshit Go v2',
        author='Ankit Dhiman',
        description='Another random description',
        rating=10
    )

    Books[str(find_key_256(book1.id))] = book1
    Books[str(find_key_256(book2.id))] = book2
    Books[str(find_key_256(book3.id))] = book3
    Books[str(find_key_256(book4.id))] = book4
    Books[str(find_key_256(book5.id))] = book5

def find_key_256(uuid):
    id = str(uuid)
    k = sha256(id.encode())
    return k.hexdigest()