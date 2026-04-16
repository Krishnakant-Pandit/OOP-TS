import json

FILE = "products.json"

def load_products():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_products(products):
    with open(FILE, "w") as f:
        json.dump(products, f, indent=4)