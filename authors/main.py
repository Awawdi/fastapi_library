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
    return set(result)


def load_file(selected_file : str = LIBRARY_JSON_FILE):
     with open(selected_file, "r") as dummy_file:
        return json.load(dummy_file)["books"]
        
     
    
