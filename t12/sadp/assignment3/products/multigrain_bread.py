from .product import Product


class MultigrainBread(Product):
    price = 125

    def __init__(self):
        print(f"Baking Multigrain Bread worth Rs.{self.price}")
