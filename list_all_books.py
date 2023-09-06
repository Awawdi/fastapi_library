import json

LIBRARY_JSON_FILE = "library.json"

def load_file():
     with open(LIBRARY_JSON_FILE, "r") as dummy_file:
         return json.load(dummy_file)

def read_item_by_id(item_id:str):
    with open(LIBRARY_JSON_FILE, "r") as dummy_file:
        all_books_list = json.load(dummy_file)["books"]
        res = [d for d in all_books_list if d.get("isbn",None) == item_id]
        return res[0]

if __name__ == "__main__":
    print(read_item_by_id("9781491943533"))