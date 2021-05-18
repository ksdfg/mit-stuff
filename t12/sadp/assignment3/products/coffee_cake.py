from .product import Product


class CoffeeCake(Product):
    price = 200

    def __init__(self):
        print(f"Baking a Coffee Cake worth ₹{self.price}")
