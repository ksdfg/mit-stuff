from .product import Product


class ElaichiBiscuits(Product):
    selling_price = 50
    cost_price = 20

    def __init__(self):
        print(f"Baking Elaichi Biscuits worth ₹{self.selling_price}, operation costs ₹{self.cost_price}")
