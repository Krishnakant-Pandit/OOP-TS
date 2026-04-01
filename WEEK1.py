print("Onlne Order System - Week 1")

customer = input("Enter customer name: ")
product = input("Enter product name: ")
qty = int(input("Enter quantity: "))
price = float(input("Enter price per unit: "))

if qty <= 0:
    print("Quntity must be greater than 0")
else:
    total = qty * price
    print("\n----- Order Recipt -----")
    print("Customer:", customer)
    print("Product:", product)
    print("Quantity:", qty)
    print("Price:", price)
    print("Total Amount:", total)