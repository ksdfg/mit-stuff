from .product import Product


class BuorbonBiscuits(Product):
    selling_price = 50
    cost_price = 20

    def __init__(self):
        print(f"Baking Buorbon Biscuits worth ₹{self.selling_price}, operation costs ₹{self.cost_price}")
