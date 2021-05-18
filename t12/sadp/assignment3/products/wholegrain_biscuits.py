from .product import Product


class WholegrainBiscuits(Product):
    price = 50

    def __init__(self):
        print(f"Baking Wholegrain Biscuits worth ₹{self.price}")
