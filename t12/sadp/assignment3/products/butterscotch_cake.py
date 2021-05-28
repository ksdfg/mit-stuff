from .product import Product


class ButterscotchCake(Product):
    selling_price = 200
    cost_price = 150

    def __init__(self):
        print(f"Baking a Buttercotch Cake worth ₹{self.selling_price}, operation costs ₹{self.cost_price}")
