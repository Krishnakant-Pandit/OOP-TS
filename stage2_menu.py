orders = []

while True:
    print("\n1. Place Order\n2. View Orders\n3. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Customer: ")
        product = input("Product: ")
        qty = int(input("Qty: "))
        price = float(input("Price: "))

        total = qty * price
        orders.append([name, product, qty, price, total])

    elif choice == "2":
        for o in orders:
            print(o)

    elif choice == "3":
        break
