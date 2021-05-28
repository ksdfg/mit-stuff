from assignment3.bakery import BakeryOutlet
from assignment3.products import product_classes


if __name__ == "__main__":
    print("Types of products that a bakery can create")
    for product_class in product_classes.keys():
        print(f"- {product_class}")

    bakery_outlet = BakeryOutlet(name="MIT Bakery Outlet")
    print("\nCreated", bakery_outlet)

    print("\nTrying to create another bakery outlet")
    bakery_outlet = BakeryOutlet("MIT WPU Bakery Outlet")
    print(f"Existing instance of BakeryOutlet is {BakeryOutlet.get_instance()}")

    print("\nAdding a few products to the Bakery Outlet's inventory")
    bakery_outlet.create_product("Butterscotch Cake")
    bakery_outlet.create_product("Pita Bread")
    bakery_outlet.create_product("Buorbon Biscuits")

    print("\n", bakery_outlet.list_products(), sep="")

    print("\nSelling second product in inventory")
    print(f"Product sold = {bakery_outlet.sell_product(1)}")

    print("\n", bakery_outlet.list_products(), sep="")

    print("\nAdd more products to the Bakery Outlet's inventory")
    bakery_outlet.create_product("Wholegrain Biscuits")
    bakery_outlet.create_product("Truffle Cake")

    print("\n", bakery_outlet.list_products(), sep="")
