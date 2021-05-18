from .product import Product


class BuorbonBiscuits(Product):
    price = 50

    def __init__(self):
        print(f"Baking Buorbon Biscuits worth ₹{self.price}")
