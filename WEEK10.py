import json
import pandas as pd
import numpy as np

file = "orders.json"

try:
    with open(file, "r") as f:
        data = json.load(f)
except:
    print("File not found or empty")
    data = []

if len(data) == 0:
    print("No data to analyse")
else:
    df = pd.DataFrame(data)

    print("Columns in file:", df.columns)
    print()

    if "total" not in df.columns:
        if "price" in df.columns and "qty" in df.columns:
            df["total"] = df["price"] * df["qty"]
        else:
            print("Required data missing (price/qty)")
            exit()

    print("Total no. of orders:", len(df))
    print()

    total_revenue = np.sum(df["total"])
    print("Total revnue:", total_revenue)
    print()

    avg_value = np.mean(df["total"])
    print("Avg order value:", avg_value)
    print()

    print("Most sold product:")
    if "product" in df.columns:
        print(df["product"].value_counts().head(1))
    else:
        print("Product data not found")

    print()