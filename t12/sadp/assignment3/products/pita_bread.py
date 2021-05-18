from .product import Product


class PitaBread(Product):
    price = 125

    def __init__(self):
        print(f"Baking Pita bread worth ₹{self.price}")
