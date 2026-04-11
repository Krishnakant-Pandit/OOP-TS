import pandas as pd
import numpy as np

def generate_report(orders):
    if not orders:
        print("No data for report\n")
        return

    df = pd.DataFrame.from_dict(orders, orient='index')

    print("\n----- REPORT -----\n")

    print(f"{'ID':<8}{'Name':<15}{'Product':<15}{'Qty':<5}{'Total':<10}{'Status':<12}")
    print("-" * 70)

    for oid, row in df.iterrows():
        print(f"{oid:<8}{row['name']:<15}{row['product']:<15}{row['qty']:<5}{row['total']:<10}{row['status']:<12}")

    total_orders = len(df)
    total_revenue = np.sum(df["total"])
    total_quantity = np.sum(df["qty"])

    print("\nSummary:")
    print("Total Orders:", total_orders)
    print("Total Quantity:", total_quantity)
    print("Total Revenue:", total_revenue)
    print("------------------\n")