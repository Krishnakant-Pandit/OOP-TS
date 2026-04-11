def display_products(products):
    if not products:
        print("No products available\n")
        return

    print("\nAvailable Products:\n")
    print(f"{'ID':<10}{'Name':<20}{'Price':<10}")
    print("-" * 40)

    for pid, data in products.items():
        print(f"{pid:<10}{data['name']:<20}{data['price']:<10}")

    print()