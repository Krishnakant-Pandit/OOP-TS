orders = {}

def add_order():
    oid = input("Enter order id: ")
    cust = input("Enter customer: ")
    prod = input("Enter product: ")
    qty = int(input("Enter quantity: "))
    price = float(input("Enter price: "))

    orders[oid] = {
        "customer": cust,
        "product": prod,
        "quantity": qty,
        "price": price,
        "status": "Placed"
    }

    print("Order stored sucesfully")

def show_orders():
    if len(orders) == 0:
        print("No recods avilable")
    else:
        for oid in orders:
            print(oid, orders[oid])


while True:
    print("\n1 Add Order")
    print("2 Show Orders")
    print("3 Exit")

    ch = input("Enter choice: ")

    if ch == "1":
        add_order()
    elif ch == "2":
        show_orders()
    elif ch == "3":
        break