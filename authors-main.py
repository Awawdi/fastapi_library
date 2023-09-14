import json
from fastapi import FastAPI

LIBRARY_JSON_FILE = "library.json"

app = FastAPI()

@app.get("/")
async def root():
    return load_file()

@app.get("/authors")
async def read_all_authors():
    all_books_list = load_file()
    result = [d.get("author",None) for d in all_books_list]
    if not result:
        raise Exception("No author was found!.")
    return set(result)

@app.get("/authors/{item_id}")
async def read_item(item_id):
    all_books_list = load_file()
    result = [d for d in all_books_list if d.get("author",None) == item_id]
    if not result:
        raise Exception(f"Author {item_id} was found!.")
    return result[0]

def load_file(selected_file : str = LIBRARY_JSON_FILE):
     with open(selected_file, "r") as dummy_file:
        return json.load(dummy_file)["books"]
        
     
    
