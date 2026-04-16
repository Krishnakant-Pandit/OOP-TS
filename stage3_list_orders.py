orders = []

def add_order():
    name = input("Customer: ")
    product = input("Product: ")
    qty = int(input("Qty: "))
    price = float(input("Price: "))
    orders.append([name, product, qty, price])

def search():
    name = input("Search customer: ").lower()
    for o in orders:
        if name in o[0].lower():
            print(o)

while True:
    print("\n1 Add\n2 View\n3 Search\n4 Exit")
    ch = input()

    if ch == "1":
        add_order()
    elif ch == "2":
        for o in orders:
            print(o)
    elif ch == "3":
        search()
    else:
        break
