import json
from fastapi import FastAPI
from pathlib import Path
import os

LIBRARY_JSON_FILE = "library.json"

app = FastAPI()

@app.get("/")
async def root():
    return load_file()

@app.get("/books")
async def read_all_books():
    all_books_list = load_file()
    result = [d.get("title",None) for d in all_books_list]
    return set(result)

@app.get("/books/{item_id}")
async def read_item(item_id):
    all_books_list = load_file()
    res = [d for d in all_books_list if d.get("isbn",None) == item_id]
    return res[0]

def load_file(selected_file : str = LIBRARY_JSON_FILE):
     with open(selected_file, "r") as dummy_file:
        return json.load(dummy_file)["books"]
        
     
    
