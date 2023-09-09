import json

LIBRARY_JSON_FILE = "library.json"

def load_file(selected_file : str = LIBRARY_JSON_FILE):
     with open(selected_file, "r") as dummy_file:
        temp = json.dumps(dummy_file)
        print(temp)

def read_all_authors():
    all_books_list = load_file()
    result = [d.get("author",None) for d in all_books_list]
    return set(result)

if __name__ == "__main__":
    print(read_all_authors())