from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello_wordl():
    return 'Hello World'

@app.get("/number/{number}")
def add_number(number: int):
    result = number
    return result
