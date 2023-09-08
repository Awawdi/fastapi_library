import json

LIBRARY_JSON_FILE = "library.json"

def load_file():
     with open(LIBRARY_JSON_FILE, "r") as dummy_file:
         return json.load(dummy_file)

def read_all_authors():
    with open(LIBRARY_JSON_FILE, "r") as dummy_file:
        all_books_list = json.load(dummy_file)["books"]
        result = [d.get("author",None) for d in all_books_list]
        return set(result)

if __name__ == "__main__":
    print(read_all_authors())