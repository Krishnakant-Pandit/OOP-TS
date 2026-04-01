class Order:
    def __init__(self, oid, cust, prod, qty, price):
        self.oid = oid
        self.cust = cust
        self.prod = prod
        self.qty = qty
        self.price = price
        self.status = "Placed"

    def total(self):
        return self.qty * self.price

    def display(self):
        print("Order ID:", self.oid)
        print("Customer:", self.cust)
        print("Product:", self.prod)
        print("Status:", self.status)


orders = []

def add_order():
    oid = input("Enter order id: ")
    cust = input("Enter customer: ")
    prod = input("enter product: ")
    qty = int(input("Enter qty: "))
    price = float(input("Enter price: "))

    o = Order(oid, cust, prod, qty, price)
    orders.append(o)
    print("Order object creatd")

def show_orders():
    if len(orders) == 0:
        print("No orders found")
    else:
        for o in orders:
            o.display()


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