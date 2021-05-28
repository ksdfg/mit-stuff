from .product import Product


class PitaBread(Product):
    selling_price = 125
    cost_price = 80

    def __init__(self):
        print(f"Baking Pita bread worth ₹{self.selling_price}, operation costs ₹{self.cost_price}")
