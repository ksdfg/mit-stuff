from typing import Optional

from assignment3.bakery.bakery import Bakery
from assignment3.products import Product


class BakeryProxy:
    bakeries: list[Bakery]

    def __init__(self, no_of_bakeries: int = 2, initial_funding: int = 200):
        """
        :param no_of_bakeries: How many bakeries should the proxy control
        :param initial_funding: How much funds should each bakery have initially
        """
        self.bakeries = [Bakery(name=f"Bakery {i}", funds=initial_funding) for i in range(no_of_bakeries)]

    def bake(self, product_type) -> Optional[Product]:
        """
        Order one of the bakeries to bake a product
        :param product_type: Type of product to bake
        :return: Baked product
        """
        self.bakeries.sort(key=lambda x: x.funds, reverse=True)
        return self.bakeries[0].bake(product_type)
