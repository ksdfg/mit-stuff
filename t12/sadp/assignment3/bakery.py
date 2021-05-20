from typing import Optional

from assignment3.products import Product
from assignment3.product_factory import ProductFactory


class Bakery(object):
    name: str
    products: list[Product] = []

    __instance = None
    _product_factory = ProductFactory()

    def __init__(self, name: str):
        if self.__instance is not None:
            print("This is a singleton class, and an instance already exists!")
        else:
            self.name = name
            Bakery.__instance = self

    @staticmethod
    def get_instance():
        """
        :return: Singleton instance of Bakery class
        """
        return Bakery.__instance

    def create_product(self, product_type: str):
        """
        Create a product of the specified type and add it to our list of products
        :param product_type: Type of product to be created e.g. WholegrainBiscuits, TruffleCake etc.
        :return: Nothing
        """
        product = self._product_factory.create(product_type)
        if product:
            self.products.append(product)

    def sell_product(self, product_index: int) -> Optional[Product]:
        """
        Sell product present at index number given in the bakery's list of products
        :param product_index: Index at which product to be sold is present in Bakery object's list of products
        :return: Product that has been sold
        """
        product = None

        try:
            product = self.products[product_index]
            self.products.remove(product)
        except IndexError:
            print("We do not have that many products!")

        return product

    def __repr__(self):
        """
        :return: String that represents a Bakery object textually
        """
        return f"<Bakery '{self.name}'>"
