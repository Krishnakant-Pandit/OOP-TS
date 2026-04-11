class Order:
    def __init__(self, oid, name, product, qty, price):
        self.oid = oid
        self.name = name
        self.product = product
        self.qty = qty
        self.price = price
        self.status = "Placed"

    def total(self):
        return self.qty * self.price

    def to_dict(self):
        return {
            "name": self.name,
            "product": self.product,
            "qty": self.qty,
            "price": self.price,
            "total": self.total(),
            "status": self.status
        }