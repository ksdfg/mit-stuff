from typing import Optional

from assignment3.product_factory import ProductFactory, FundsError
from assignment3.products import Product


class Bakery:
    name: str
    funds: int

    _product_factory = ProductFactory()

    def __init__(self, name: str, funds: int):
        self.name = name
        self.funds = funds

    def bake(self, product_type: str) -> Optional[Product]:
        """
        Bake a product
        :param product_type: What type of Product to bake
        :return: Baked Product
        """
        try:
            product = self._product_factory.create(product_type, self.funds)
            self.funds -= product.cost_price
            print(f"{self.name}'s funds are now ₹{self.funds}")
            return product
        except FundsError:
            print(f"{self.name} doesn't have enough funds to make a {product_type}")

    def __repr__(self) -> str:
        """
        :return: String that represents a BakeryOutlet object textually
        """
        return f"<Bakery '{self.name}'>"
