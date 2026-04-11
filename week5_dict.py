def add_order_dict(orders, order_id, data):
    if order_id in orders:
        print("Order ID already exists! Cannot overwrite.\n")
        return False
    else:
        orders[order_id] = data
        return True