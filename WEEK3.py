orders = []

while True:
    print("\n--- Order Menu ---")
    print("1. Place Order")
    print("2. View Orders")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        cust = input("Enter customer name: ")
        prod = input("Enter product name: ")
        qty = int(input("Enter quantity: "))
        price = float(input("Enter price: "))

        total = qty * price
        orders.append([cust, prod, qty, price, total])

        print("Order placed succesfully")

    elif choice == "2":
        if len(orders) == 0:
            print("No orders avilable")
        else:
            print("All Orders:")
            for o in orders:
                print(o)

    elif choice == "3":
        print("Exiting program")
        break

    else:
        print("Invalid choise")