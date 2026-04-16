from storage.json_store import save, load
from storage.product_store import load_products, save_products
from analysis.analyzer import analyze
from utils.error_handlers import handle_error

# Load data
orders = load()
products = load_products()

def show_products():
    import pandas as pd
    import numpy as np

    if not products:
        print("No products available!")
        return

    df = pd.DataFrame(products)

    df.index = np.arange(1, len(df) + 1)
    df.index.name = "Product_ID"

    df = df[["name", "price", "category"]]

    print("\n===== PRODUCT LIST =====")
    print(df.to_string())

def add_product():
    try:
        name = input("Product name: ")
        price = float(input("Price: "))
        category = input("Category: ")

        products.append({
            "name": name,
            "price": price,
            "category": category
        })

        save_products(products)
        print("Product Added!")

    except Exception as e:
        handle_error(e)

def delete_product():
    try:
        show_products()
        idx = int(input("Enter product number to delete: ")) - 1

        if 0 <= idx < len(products):
            products.pop(idx)
            save_products(products)
            print("Product Deleted!")
        else:
            print("Invalid selection!")

    except Exception as e:
        handle_error(e)

def make_order():
    try:
        show_products()
        choice = int(input("Select product number: ")) - 1
        qty = int(input("Enter Quantity: "))
        customer = input("Enter Your Name: ")

        product = products[choice]

        if not orders:
            new_id = 1001
        else:
            new_id = max([o["order_id"] for o in orders]) + 1

        total_price = qty * product["price"]

        order = {
            "order_id": new_id,
            "customer": customer,
            "product": product["name"],
            "quantity": qty,
            "price": product["price"],
            "category": product["category"],
            "status": "Placed",
            "total": total_price
        }

        orders.append(order)
        save(orders)

        print("\n===== ORDER CONFIRMATION =====")
        print("Order ID:", new_id)
        print("Product:", product["name"])
        print("Quantity:", qty)
        print("Price per item:", product["price"])
        print("Total Price: ₹", total_price)

    except Exception as e:
        handle_error(e)

def show_orders():
    import pandas as pd
    import numpy as np

    if not orders:
        print("No orders found!")
        return

    df = pd.DataFrame(orders)

    # Set proper column order
    df = df[["order_id", "customer", "product", "quantity",
             "price", "category", "status", "total"]]

    # Set index using NumPy (clean numbering)
    df.index = np.arange(1, len(df) + 1)
    df.index.name = "No"

    print("\n===== ALL ORDERS (SHOPKEEPER VIEW) =====")
    print(df.to_string())

def order_history():
    import pandas as pd
    import numpy as np

    if not orders:
        print("No orders available!")
        return

    df = pd.DataFrame(orders)

    df = df[["order_id", "customer", "product", "quantity",
             "price", "category", "status", "total"]]

    print("\n===== ORDER HISTORY =====")
    print(df.to_string(index=False))

    totals = np.array(df["total"])
    print("\nTotal Money Spended:", np.sum(totals))
    print("Average Order Value:", np.mean(totals))

def update_status():
    try:
        oid = int(input("Enter Order ID: "))
        for o in orders:
            if o["order_id"] == oid:
                print("\n1. Packed\n2. Shipped\n3. Delivered\n4. Cancelled")
                ch = input("Select new status: ")

                status_map = {
                    "1": "Packed",
                    "2": "Shipped",
                    "3": "Delivered",
                    "4": "Cancelled"
                }

                if ch in status_map:
                    o["status"] = status_map[ch]
                    print("Status Updated!")
                else:
                    print("Invalid choice!")
                return

        print("Order not found!")

    except Exception as e:
        handle_error(e)

def delete_order():
    try:
        oid = int(input("Enter Order ID to delete: "))
        for o in orders:
            if o["order_id"] == oid:
                orders.remove(o)
                print("Order Deleted!")
                return

        print("Order not found!")

    except Exception as e:
        handle_error(e)


def search_order():
    key = input("Enter search keyword: ").lower()
    found = False

    for o in orders:
        if key in o["customer"].lower() or key in o["product"].lower():
            print(o)
            found = True

    if not found:
        print("No matching orders!")


def track_shipment():
    try:
        oid = int(input("Enter Order ID: "))
        for o in orders:
            if o["order_id"] == oid:
                print(f"Current Status: {o['status']}")
                return

        print("Order not found!")

    except Exception as e:
        handle_error(e)


def generate_report():
    if not orders:
        print("No data to analyze!")
        return
    analyze(orders)


def customer_menu():
    while True:
        print("\n--- CUSTOMER MENU ---")
        print("1. Show Products")
        print("2. Make Order")
        print("3. Track Shipment")
        print("4. Order History")
        print("5. Back")

        ch = input("Enter choice: ")

        if ch == "1":
            show_products()
        elif ch == "2":
            make_order()
        elif ch == "3":
            track_shipment()
        elif ch == "4":
            order_history()
        elif ch == "5":
            break
        else:
            print("Invalid choice!")

def shopkeeper_menu():
    while True:
        print("\n--- SHOPKEEPER MENU ---")
        print("1. Show Orders")
        print("2. Add Product")
        print("3. Delete Product")
        print("4. Update Status")
        print("5. Search Order")
        print("6. Delete Order")
        print("7. Generate Report")
        print("8. Show Products")
        print("9. Back")

        ch = input("Enter choice: ")

        if ch == "1":
            show_orders()
        elif ch == "2":
            add_product()
        elif ch == "3":
            delete_product()
        elif ch == "4":
            update_status()
        elif ch == "5":
            search_order()
        elif ch == "6":
            delete_order()
        elif ch == "7":
            generate_report()
        elif ch == "8":
            show_products()
        elif ch == "9":
            save(orders)
            save_products(products)
            print("Data Saved!")
            break
        else:
            print("Invalid choice!")


def role_menu():
    while True:
        print("\n1. Customer\n2. Shopkeeper\n3. Exit")
        ch = input("Choose: ")

        if ch == "1":
            customer_menu()
        elif ch == "2":
            pwd = input("Enter Password: ")
            if pwd == "admin123":
                shopkeeper_menu()
            else:
                print("Wrong Password!")
        elif ch == "3":
            save(orders)
            save_products(products)
            print("Saved & Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    role_menu()