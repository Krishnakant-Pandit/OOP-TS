def update_status(orders, order_id):
    if order_id in orders:
        new_status = input("Enter new status (Shipped/Delivered): ")
        orders[order_id]["status"] = new_status
        print("Order updated successfully!\n")
    else:
        print("Order not found!\n")