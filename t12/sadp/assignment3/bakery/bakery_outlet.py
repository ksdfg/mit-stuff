from typing import Optional

from assignment3.bakery_proxy import BakeryProxy
from assignment3.products import Product


class BakeryOutlet(object):
    name: str
    products: list[Product] = []

    __instance = None
    _proxy = BakeryProxy()

    def __init__(self, name: str):
        if self.__instance is not None:
            print("This is a singleton class, and an instance already exists!")
        else:
            self.name = name
            BakeryOutlet.__instance = self

    @staticmethod
    def get_instance():
        """
        :return: Singleton instance of BakeryOutlet class
        """
        return BakeryOutlet.__instance

    def create_product(self, product_type: str):
        """
        Create a product of the specified type and add it to our list of products
        :param product_type: Type of product to be created e.g. WholegrainBiscuits, TruffleCake etc.
        :return: Nothing
        """
        product = self._proxy.bake(product_type)
        if product:
            self.products.append(product)

    def sell_product(self, product_index: int) -> Optional[Product]:
        """
        Sell product present at index number given in the bakery's list of products
        :param product_index: Index at which product to be sold is present in BakeryOutlet object's list of products
        :return: Product that has been sold
        """
        product = None

        try:
            product = self.products[product_index]
            self.products.remove(product)
        except IndexError:
            print("We do not have that many products!")

        return product

    def list_products(self) -> str:
        """
        :return: All the products in the BakeryOutlet object's list of products as a formatted string
        """
        ret = f"Bakery Outlet's inventory as of now:"
        for product in self.products:
            ret += f"\n- {product}"
        return ret

    def __repr__(self) -> str:
        """
        :return: String that represents a BakeryOutlet object textually
        """
        return f"<Bakery Outlet '{self.name}'>"
