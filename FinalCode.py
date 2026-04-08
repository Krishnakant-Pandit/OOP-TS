# ONLINE ORDER PROCESSING & TRACKING SYSTEM
# FINAL UPDATED CODE (with formatting + qty + total)

import json
import pandas as pd
import numpy as np


class Order:
    def __init__(self, order_id, customer, product, price, quantity):
        self.order_id = order_id
        self.customer = customer
        self.product = product
        self.price = price
        self.quantity = quantity
        self.status = "Placed"

    def total_price(self):
        return self.price * self.quantity

    def to_dict(self):
        return {
            "order_id": self.order_id,
            "customer": self.customer,
            "product": self.product,
            "price": self.price,
            "quantity": self.quantity,
            "status": self.status
        }


class OrderSystem:
    def __init__(self):
        self.orders = {}
        self.load_from_file()

    # ---------- FILE ----------
    def save_to_file(self):
        data = {oid: o.to_dict() for oid, o in self.orders.items()}
        with open("orders.json", "w") as f:
            json.dump(data, f)

    def load_from_file(self):
        try:
            with open("orders.json", "r") as f:
                data = json.load(f)
                for oid, d in data.items():
                    o = Order(d["order_id"], d["customer"], d["product"],
                              d["price"], d["quantity"])
                    o.status = d["status"]
                    self.orders[oid] = o
        except:
            print("No previous data found...\n")

    # ---------- ADD ----------
    def add_order(self):
        oid = input("Enter Order ID: ")

        if oid in self.orders:
            print("Order alredy exist!!\n")
            return

        name = input("Enter customer name: ")
        product = input("Enter product name: ")

        try:
            price = float(input("Enter price per item: "))
            qty = int(input("Enter how much quantity needed: "))
        except:
            print("Invalid input!!\n")
            return

        o = Order(oid, name, product, price, qty)
        self.orders[oid] = o
        self.save_to_file()

        print("Order added succesfully")
        print("Total Price:", o.total_price(), "\n")

    # ---------- VIEW ----------
    def view_orders(self):
        if not self.orders:
            print("No records found!!\n")
            return

        for o in self.orders.values():
            print("------------------")
            print("Order ID:", o.order_id)
            print("Customer:", o.customer)
            print("Product:", o.product)
            print("Quantity:", o.quantity)
            print("Total Price:", o.total_price())
            print("Status:", o.status)
            print()

    # ---------- UPDATE ----------
    def update_status(self):
        oid = input("Enter Order ID: ")

        if oid not in self.orders:
            print("Order not found\n")
            return

        print("1.Packed  2.Shipped  3.Delivered")
        ch = input("Enter choice: ")

        if ch == "1":
            self.orders[oid].status = "Packed"
        elif ch == "2":
            self.orders[oid].status = "Shipped"
        elif ch == "3":
            self.orders[oid].status = "Delivered"
        else:
            print("Wrong input\n")
            return

        self.save_to_file()
        print("Status updated\n")

    # ---------- SEARCH ----------
    def search_order(self):
        oid = input("Enter Order ID: ")
        o = self.orders.get(oid)

        if not o:
            print("Order not found!!\n")
            return

        print("Customer:", o.customer)
        print("Product:", o.product)
        print("Quantity:", o.quantity)
        print("Total Price:", o.total_price())
        print("Status:", o.status)
        print()

    # ---------- DELETE ----------
    def delete_order(self):
        oid = input("Enter Order ID: ")

        if oid in self.orders:
            del self.orders[oid]
            self.save_to_file()
            print("Deleted successfully\n")
        else:
            print("Order not found\n")

    # ---------- SORT ----------
    def sort_orders(self):
        if not self.orders:
            print("No data to sort\n")
            return

        sorted_orders = sorted(self.orders.values(), key=lambda x: x.total_price())

        print("Sorted Orders:")
        for o in sorted_orders:
            print(o.order_id, "-", o.total_price())
        print()

    # ---------- REPORT ----------
    def generate_report(self):
        if not self.orders:
            print("No data for report\n")
            return

        data = []
        for o in self.orders.values():
            data.append([
                o.order_id, o.customer, o.product,
                o.price, o.quantity, o.total_price(), o.status
            ])

        df = pd.DataFrame(data, columns=[
            "OrderID", "Customer", "Product",
            "Price", "Qty", "Total", "Status"
        ])

        print("------ REPORT ------")
        print(df, "\n")

        totals = np.array(df["Total"])

        print("Total Revenue:", totals.sum())
        print("Average Order:", totals.mean())
        print("Max Order:", totals.max())
        print("Min Order:", totals.min())
        print()

    # ---------- FILTER ----------
    def filter_by_status(self):
        status = input("Enter status: ")

        found = False
        for o in self.orders.values():
            if o.status.lower() == status.lower():
                print(o.order_id, o.customer, o.status)
                found = True

        if not found:
            print("No matching records")
        print()


# ---------- MAIN ----------
def main():
    system = OrderSystem()

    while True:
        print("====== MENU ======")
        print("1.Add Order")
        print("2.View Orders")
        print("3.Update Status")
        print("4.Search Order")
        print("5.Delete Order")
        print("6.Sort Orders")
        print("7.Generate Report")
        print("8.Filter by Status")
        print("9.Exit")

        ch = input("Enter choice: ")

        if ch == "1":
            system.add_order()
        elif ch == "2":
            system.view_orders()
        elif ch == "3":
            system.update_status()
        elif ch == "4":
            system.search_order()
        elif ch == "5":
            system.delete_order()
        elif ch == "6":
            system.sort_orders()
        elif ch == "7":
            system.generate_report()
        elif ch == "8":
            system.filter_by_status()
        elif ch == "9":
            print("Exiting program...\n")
            break
        else:
            print("Invalid choice!!\n")


if __name__ == "__main__":
    main()