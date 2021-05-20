from assignment3 import Bakery
from assignment3.products import product_classes


def print_bakery_inventory(bakery: Bakery):
    print("\nBakery's inventory as of now:")
    for product in bakery.products:
        print(f"- {product}")


if __name__ == "__main__":
    print("Types of products that a bakery can create")
    for product_class in product_classes.keys():
        print(f"- {product_class}")

    bakery = Bakery(name="MIT Bakery")
    print("\nCreated", bakery)

    print("\nTrying to create another bakery")
    bakery = Bakery("MIT WPU Bakery")
    print(f"Existing instance of Bakery is {Bakery.get_instance()}")

    print("\nAdding a few products to the Bakery's inventory")
    bakery.create_product("Butterscotch Cake")
    bakery.create_product("Pita Bread")
    bakery.create_product("Buorbon Biscuits")

    print_bakery_inventory(bakery)

    print("\nSelling second product in inventory")
    print(f"Product sold = {bakery.sell_product(1)}")

    print_bakery_inventory(bakery)

    print("\nAdd another product to the Bakery's inventory")
    bakery.create_product("Wholegrain Biscuits")

    print_bakery_inventory(bakery)
