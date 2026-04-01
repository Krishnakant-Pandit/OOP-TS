class OrderTracking:
    def __init__(self):
        self.orders = {}

    def add_order(self):
        oid = input("Enter Order ID: ")
        cust = input("Enter Customer: ")
        prod = input("Enter Product: ")

        self.orders[oid] = {
            "customer": cust,
            "product": prod,
            "status": "Placed"
        }

        print("Order added succesfully")

    def update_status(self):
        oid = input("Enter Order ID: ")
        if oid in self.orders:
            st = input("Enter new status: ")
            self.orders[oid]["status"] = st
            print("Status updatd")
        else:
            print("Order not found")

    def show_orders(self):
        if len(self.orders) == 0:
            print("No orders avilable")
        else:
            for oid in self.orders:
                print(oid, self.orders[oid])


def menu():
    sys = OrderTracking()

    while True:
        print("\n1 Add Order")
        print("2 Update Status")
        print("3 Show Orders")
        print("4 Exit")

        ch = input("Enter choice: ")

        if ch == "1":
            sys.add_order()
        elif ch == "2":
            sys.update_status()
        elif ch == "3":
            sys.show_orders()
        elif ch == "4":
            break

menu()