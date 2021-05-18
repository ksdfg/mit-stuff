from .product import Product


class TruffleCake(Product):
    price = 200

    def __init__(self):
        print(f"Baking a Truffle Cake worth ₹{self.price}")
