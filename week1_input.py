from week11_exceptions import safe_int

def get_customer_details():
    name = input("Enter Customer Name: ")

    while True:
        qty = safe_int(input("Enter Quantity: "))
        if qty > 0:
            break
        else:
            print("Quantity must be greater than 0! Try again.\n")

    return name, qty