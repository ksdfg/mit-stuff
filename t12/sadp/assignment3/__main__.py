from assignment3 import Bakery

if __name__ == "__main__":
    bakery = Bakery(name="Test Bakery")
    print(bakery)

    bakery.create_product("TruffleCake")
    print(bakery.products)
