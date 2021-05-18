from .product import Product


class WholeWheatBread(Product):
    price = 125

    def __init__(self):
        print(f"Baking Whole Wheat Bread worth ₹{self.price}")
