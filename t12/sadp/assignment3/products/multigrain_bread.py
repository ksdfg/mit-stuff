from .product import Product


class MultigrainBread(Product):
    selling_price = 125
    cost_price = 80

    def __init__(self):
        print(f"Baking Multigrain Bread worth ₹{self.selling_price}, operation costs ₹{self.cost_price}")
