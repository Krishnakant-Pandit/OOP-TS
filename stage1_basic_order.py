customer = input("Enter Customer Name: ")
product = input("Enter Product Name: ")
quantity = int(input("Enter Quantity: "))
price = float(input("Enter Price: "))

if quantity <= 0:
    print("Invalid quantity")
else:
    total = quantity * price
    print("\n--- Order Receipt ---")
    print("Customer:", customer)
    print("Product:", product)
    print("Total:", total)
