orders = []

def calculate_total(qty, price):
    return qty * price

def add_order():
    cust = input("Enter customer: ")
    prod = input("Enter product: ")
    qty = int(input("Enter quantity: "))
    price = float(input("Enter price: "))

    total = calculate_total(qty, price)
    orders.append([cust, prod, qty, price, total])

    print("Order added succesfully")

def list_orders():
    if len(orders) == 0:
        print("No orders available")
    else:
        for o in orders:
            print(o)

def update_status():
    name = input("Entre customer name: ")
    print("Status updatd for", name)


while True:
    print("\n1 Add Order")
    print("2 List Orders")
    print("3 Update Status")
    print("4 Exit")

    ch = input("Choice: ")

    if ch == "1":
        add_order()
    elif ch == "2":
        list_orders()
    elif ch == "3":
        update_status()
    elif ch == "4":
        break