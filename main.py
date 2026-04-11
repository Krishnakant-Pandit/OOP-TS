import json

from week1_input import get_customer_details
from week2_menu import main_menu
from week3_products import display_products
from week4_validation import validate_product
from week7_tracking import track_order
from week8_json import load, save
from week9_search import search_order
from week10_status import update_status
from week11_exceptions import safe_int
from week12_report import generate_report


orders = load("orders.json")
products = load("products.json")

# Auto order ID
if orders:
    next_order_id = max(int(i) for i in orders.keys()) + 1
else:
    next_order_id = 1001


while True:
    print("\n===== MAIN MENU =====")
    print("1. Customer")
    print("2. Shopkeeper")
    print("3. Exit")

    role = input("Enter choice: ")

    if role == "1":
        while True:
            print("\n--- CUSTOMER MENU ---")
            print("1. Show Products")
            print("2. Make Order")
            print("3. Track Shipment")
            print("4. Order History")
            print("5. Back")

            choice = input("Enter choice: ")

            if choice == "1":
                display_products(products)

            elif choice == "2":
                if not products:
                    print("No products available\n")
                    continue

                display_products(products)

                pid = input("Enter Product ID: ")

                if pid not in products:
                    print("Invalid Product ID\n")
                    continue

                name, qty = get_customer_details()

                price = products[pid]["price"]
                pname = products[pid]["name"]
                total = qty * price

                order_id = str(next_order_id)
                next_order_id += 1

                orders[order_id] = {
                    "name": name,
                    "product": pname,
                    "qty": qty,
                    "price": price,
                    "total": total,
                    "status": "Placed"
                }

                save("orders.json", orders)
                print(f"Order placed successfully! Order ID: {order_id}\n")

            elif choice == "3":
                oid = input("Enter Order ID: ")
                track_order(orders, oid)

            elif choice == "4":
                if not orders:
                    print("No orders found\n")
                else:
                    print(f"\n{'ID':<8}{'Name':<15}{'Product':<15}{'Qty':<5}{'Total':<10}{'Status':<12}")
                    print("-" * 70)

                    for oid, data in orders.items():
                        print(f"{oid:<8}{data['name']:<15}{data['product']:<15}{data['qty']:<5}{data['total']:<10}{data['status']:<12}")
                    print()

            elif choice == "5":
                break

            else:
                print("Invalid choice\n")

    elif role == "2":
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

            choice = input("Enter choice: ")

            if choice == "1":
                if not orders:
                    print("No orders available\n")
                else:
                    print(f"\n{'ID':<8}{'Name':<15}{'Product':<15}{'Qty':<5}{'Total':<10}{'Status':<12}")
                    print("-" * 70)

                    for oid, data in orders.items():
                        print(f"{oid:<8}{data['name']:<15}{data['product']:<15}{data['qty']:<5}{data['total']:<10}{data['status']:<12}")
                    print()

            elif choice == "2":
                pid = input("Enter Product ID: ")

                if pid in products:
                    print("Product ID already exists!\n")
                    continue

                pname = input("Enter Product Name: ")
                price = safe_int(input("Enter Price: "))

                products[pid] = {"name": pname, "price": price}
                save("products.json", products)

                print("Product added successfully!\n")

            elif choice == "3":
                pid = input("Enter Product ID to delete: ")

                if pid in products:
                    del products[pid]
                    save("products.json", products)
                    print("Product deleted successfully!\n")
                else:
                    print("Product not found!\n")

            elif choice == "4":
                oid = input("Enter Order ID: ")
                update_status(orders, oid)
                save("orders.json", orders)

            elif choice == "5":
                oid = input("Enter Order ID: ")
                search_order(orders, oid)

            elif choice == "6":
                oid = input("Enter Order ID: ")

                if oid in orders:
                    del orders[oid]
                    save("orders.json", orders)
                    print("Order deleted successfully!\n")
                else:
                    print("Order not found!\n")

            elif choice == "7":
                generate_report(orders)

            # Show products
            elif choice == "8":
                display_products(products)

            elif choice == "9":
                break

            else:
                print("Invalid choice\n")

    elif role == "3":
        print("Exiting system...")
        break

    else:
        print("Invalid role selection\n")