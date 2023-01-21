from fastapi import FastAPI
from pydantic import BaseModel
from uuid import UUID

app = FastAPI()

class Books(BaseModel):
    id:UUID
    title:str
    author:str
    description:str
    rating:int

# Books = ['random','placeholder','text']

@app.get('/')
def read_books():
    return Books