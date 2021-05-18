from .product import Product


class ButterscotchCake(Product):
    price = 200

    def __init__(self):
        print(f"Baking a Buttercotch Cake worth ₹{self.price}")
