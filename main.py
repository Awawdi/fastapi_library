import json
from fastapi import FastAPI
from pydantic import BaseModel
import requests

LIBRARY_JSON_FILE = "library.json"

app = FastAPI()

@app.get("/")
async def root():
    return load_file(LIBRARY_JSON_FILE)

@app.get("/books")
async def read_all_books():
    with open(LIBRARY_JSON_FILE, "r") as dummy_file:
       all_books_list = json.load(dummy_file)["books"]
       result = [d.get("title",None) for d in all_books_list]
       return set(result)

@app.get("/books/{item_id}")
async def read_item(item_id):
    with open(LIBRARY_JSON_FILE, "r") as dummy_file:
        all_books_list = json.load(dummy_file)["books"]
        res = [d for d in all_books_list if d.get("isbn",None) == item_id]
        return res[0]

@app.get("/authors")
async def read_all_authors():
    with open(LIBRARY_JSON_FILE, "r") as dummy_file:
       all_books_list = json.load(dummy_file)["books"]
       result = [d.get("author",None) for d in all_books_list]
       return set(result)


def load_file(selected_file):
     with open(selected_file, "r") as dummy_file:
        return json.load(dummy_file)
     
    