import pandas as pd

def search_order(orders, order_id):
    if order_id in orders:
        df = pd.DataFrame([orders[order_id]])
        print("\nOrder Found:\n")
        print(df, "\n")
    else:
        print("Order not found!\n")