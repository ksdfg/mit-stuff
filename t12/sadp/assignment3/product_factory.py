from typing import Optional

from assignment3.products import Product, product_classes


class FundsError(Exception):
    pass


class ProductFactory:
    @staticmethod
    def create(product_type: str, bakery_funds: int) -> Optional[Product]:
        """
        Create a product of given type
        :param product_type: Type of product to be created
        :param bakery_funds: Total funds of the bakery
        :return: Created product
        """
        product = None

        try:
            product_class = product_classes[product_type]
            if product_class.cost_price > bakery_funds:
                raise FundsError
            product = product_class()
        except KeyError:
            print("Recipe for this product is unkown!")

        return product
