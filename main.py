import json
from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    price: float

LIBRARY_JSON_FILE = "library.json"

app = FastAPI()

@app.get("/")
async def root():
    return load_file(LIBRARY_JSON_FILE)

@app.get("/items/{item_id}")
async def read_item(item_id):
    with open(LIBRARY_JSON_FILE, "r") as dummy_file:
        all_books_list = json.load(dummy_file)["books"]
        res = [d for d in all_books_list if d.get("isbn",None) == item_id]
        return res[0]


def load_file(selected_file):
     with open(selected_file, "r") as dummy_file:
         return json.load(dummy_file)
     
    