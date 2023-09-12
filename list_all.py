import json
from fastapi import FastAPI
from pathlib import Path
import os

REPO_ABSPATH = Path(os.path.abspath(__file__)).parent

LIBRARY_JSON_FILE = REPO_ABSPATH / "library.json"

def read_all_authors():
    all_books_list = load_file()
    result = [d.get("author",None) for d in all_books_list]
    return set(result)


def load_file(selected_file : str = LIBRARY_JSON_FILE):
     with open(selected_file, "r") as dummy_file:
        return json.load(dummy_file)["books"]

if __name__ == "__main__":
    print (read_all_authors())
     
    
