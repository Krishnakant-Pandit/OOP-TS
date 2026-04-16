import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def analyze(data):
    if not data:
        print("No data available!")
        return

    df = pd.DataFrame(data)

    print("\n===== FULL DATA =====")
    print(df.to_string(index=False))

    totals = np.array(df["total"])

    print("\n===== ANALYTICS REPORT =====")
    print("Total Revenue:", np.sum(totals))
    print("Average Order Value:", np.mean(totals))
    print("Maximum Order Value:", np.max(totals))
    print("Minimum Order Value:", np.min(totals))

    print("\n===== CATEGORY-WISE ORDERS =====")
    print(df["category"].value_counts())

    print("\n===== TOP PRODUCTS =====")
    print(df["product"].value_counts())

    product_sales = df.groupby("product")["total"].sum()

    plt.figure()
    product_sales.plot(kind='bar')
    plt.xlabel("Products")
    plt.ylabel("Revenue")
    plt.title("Product-wise Revenue")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.show()

    plt.figure()
    df["category"].value_counts().plot(kind='pie', autopct='%1.1f%%')
    plt.title("Category Distribution")
    plt.ylabel("")
    plt.show()