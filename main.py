import json
from fastapi import FastAPI, Request


LIBRARY_JSON_FILE = "library.json"

app = FastAPI()

@app.get("/")
async def root():
    return load_file()

@app.get("/books")
async def read_all_books(request:Request):
    all_books_list = load_file()
    result = [d.get("title",None) for d in all_books_list]
    return f"Listing all books. Request coming from {request.url._url}, response: {set(result)}"

@app.get("/books/{item_id}")
async def read_item(item_id):
    all_books_list = load_file()
    res = [d for d in all_books_list if d.get("isbn",None) == item_id]
    return res[0]

@app.get("/authors")
async def read_all_authors():
    all_books_list = load_file()
    result = [d.get("author",None) for d in all_books_list]
    return set(result)


def load_file(selected_file : str = LIBRARY_JSON_FILE):
     with open(selected_file, "r") as dummy_file:
        temp = json.dumps(dummy_file)
        
     
    