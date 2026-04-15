import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def generate_report(orders):
    if not orders:
        print("No data for report\n")
        return

    # Convert to DataFrame
    df = pd.DataFrame.from_dict(orders, orient='index')

    print("\n----- REPORT -----\n")

    # Table Header
    print(f"{'ID':<8}{'Name':<15}{'Product':<15}{'Qty':<5}{'Total':<10}{'Status':<12}")
    print("-" * 70)

    # Display Data
    for oid, row in df.iterrows():
        print(f"{oid:<8}{row['name']:<15}{row['product']:<15}{row['qty']:<5}{row['total']:<10}{row['status']:<12}")

    # Summary
    total_orders = len(df)
    total_revenue = np.sum(df["total"])
    total_quantity = np.sum(df["qty"])

    print("\nSummary:")
    print("Total Orders:", total_orders)
    print("Total Quantity:", total_quantity)
    print("Total Revenue:", total_revenue)
    print("------------------\n")

    # 📊 GRAPH 1: Product-wise Sales (Revenue)
    product_sales = df.groupby("product")["total"].sum()

    plt.figure()
    product_sales.plot(kind='bar')
    plt.xlabel("Products")
    plt.ylabel("Total Revenue")
    plt.title("Product-wise Sales Report")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.show()

    plt.figure()
    product_sales.plot(kind='pie', autopct='%1.1f%%')
    plt.title("Revenue Distribution by Product")
    plt.ylabel("")
    plt.tight_layout()
    plt.show()

    status_counts = df["status"].value_counts()

    plt.figure()
    status_counts.plot(kind='bar')
    plt.xlabel("Order Status")
    plt.ylabel("Number of Orders")
    plt.title("Order Status Distribution")
    plt.tight_layout()
    plt.show()

    qty_sales = df.groupby("product")["qty"].sum()

    plt.figure()
    qty_sales.plot(kind='bar')
    plt.xlabel("Products")
    plt.ylabel("Total Quantity Sold")
    plt.title("Product-wise Quantity Sold")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.show()
