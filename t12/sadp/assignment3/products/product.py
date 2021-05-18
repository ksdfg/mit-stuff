class Product(object):
    price: int

    def __repr__(self) -> str:
        """
        :return: String that represents a Product object textually
        """
        return f"<Product {self.__class__.__name__}>"
