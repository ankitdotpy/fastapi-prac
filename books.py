from fastapi import FastAPI

app = FastAPI()

Books = {
    'book1':{
        'title':'Random Bullshit Go',
        'author': 'Ankit Dhiman',
        'year': 2023
    },
    'book2':{
        'title':'Random Bullshit Go Version 2',
        'author': 'Ankit Dhiman',
        'year': 2049
    },
    'book3':{
        'title':'Peepeepoopoo',
        'author': 'Doraemon',
        'year': 2012
    },
    'book4':{
        'title':'Haryana',
        'author': 'Ankit Dhiman',
        'year': 2044
    },
    'book5':{
        'title':'Doctor banein 30 din mein',
        'author': 'Ankit Dhiman',
        'year': 2050
    },
}

@app.get('/')
def read_all_books():
    return Books

'''
if you have a path similar to path with path parameter make sure to
implement that function before the path parameter function
otherwise it fastapi might confuse it as a path parameter
'''

@app.get('/books/all')
def read_all_books_alt():
    return Books

# Path parameters
@app.get('/book/{book_id}')
def read_book_using_id(book_id:int):
    return Books[f'book{book_id}']