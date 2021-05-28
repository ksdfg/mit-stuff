from assignment3.bakery import BakeryOutlet
from assignment3.products import product_classes


if __name__ == "__main__":
    print("Types of products that a bakery can create")
    for product_class in product_classes.keys():
        print(f"- {product_class}")

    bakery_outlet = BakeryOutlet(name="MIT Bakery")
    print("\nCreated", bakery_outlet)

    print("\nTrying to create another bakery")
    bakery_outlet = BakeryOutlet("MIT WPU Bakery")
    print(f"Existing instance of Bakery is {BakeryOutlet.get_instance()}")

    print("\nAdding a few products to the Bakery's inventory")
    bakery_outlet.create_product("Butterscotch Cake")
    bakery_outlet.create_product("Pita Bread")
    bakery_outlet.create_product("Buorbon Biscuits")

    print("\n", bakery_outlet.list_products(), sep="")

    print("\nSelling second product in inventory")
    print(f"Product sold = {bakery_outlet.sell_product(1)}")

    print("\n", bakery_outlet.list_products(), sep="")

    print("\nAdd another product to the Bakery's inventory")
    bakery_outlet.create_product("Wholegrain Biscuits")

    print("\n", bakery_outlet.list_products(), sep="")
