from .product import Product


class ElaichiBiscuits(Product):
    price = 50

    def __init__(self):
        print(f"Baking Elaichi Biscuits worth Rs.{self.price}")
