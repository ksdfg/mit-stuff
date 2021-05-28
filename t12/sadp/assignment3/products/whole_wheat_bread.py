from .product import Product


class WholeWheatBread(Product):
    selling_price = 125
    cost_price = 80

    def __init__(self):
        print(f"Baking Whole Wheat Bread worth ₹{self.selling_price}, operation costs ₹{self.cost_price}")
