import json

orders = {}

def save_orders():
    with open("orders.json", "w") as f:
        json.dump(orders, f)
    print("Orders saved succesfully")

def load_orders():
    global orders
    try:
        with open("orders.json", "r") as f:
            orders = json.load(f)
        print("Orders loaded")
    except:
        print("File not found, starting new data")

load_orders()

while True:
    print("1 Save Orders")
    print("2 Exit")

    ch = input("Enter choice: ")

    if ch == "1":
        save_orders()
    else:
        break