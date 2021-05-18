from assignment3.products import Product, get_product_class_from_name


class ProductFactory:
    @staticmethod
    def create(product_type: str) -> Product:
        """
        Create a product of given type
        :param product_type: Type of product to be created
        :return: Created product
        """
        return get_product_class_from_name(product_type)()
