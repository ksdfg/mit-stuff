from typing import Optional

from assignment3.products import Product, product_classes


class ProductFactory:
    @staticmethod
    def create(product_type: str) -> Optional[Product]:
        """
        Create a product of given type
        :param product_type: Type of product to be created
        :return: Created product
        """
        product = None

        try:
            product_class = product_classes[product_type]
            product = product_class()
        except KeyError:
            print("Recipe for this product is unkown!")

        return product
