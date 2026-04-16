import json

def save(data):
    with open("orders.json", "w") as f:
        json.dump(data, f)

def load():
    try:
        with open("orders.json", "r") as f:
            return json.load(f)
    except:
        return []
