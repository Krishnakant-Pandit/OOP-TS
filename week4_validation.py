def validate_product(pid, products):
    if pid not in products:
        print("Invalid Product ID! Please try again.\n")
        return False
    return True