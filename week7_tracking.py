def track_order(orders, order_id):
    if order_id in orders:
        print("Order Status:", orders[order_id]["status"], "\n")
    else:
        print("Order not found!\n")