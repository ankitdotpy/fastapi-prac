from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel, Field
from uuid import UUID

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

Books = []

@app.get('/')
def read_books():
    if len(Books)<1:
        create_books_no_api()
    return Books

@app.post('/')
def add_book(book:Book):
    Books.append(book)
    return book


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

    Books.append(book1)
    Books.append(book2)
    Books.append(book3)
    Books.append(book4)
    Books.append(book5)