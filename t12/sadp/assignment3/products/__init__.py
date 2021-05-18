from assignment3.products.product import Product
from assignment3.products.butterscotch_cake import ButterscotchCake
from assignment3.products.coffee_cake import CoffeeCake
from assignment3.products.truffle_cake import TruffleCake
from assignment3.products.buorbon_biscuits import BuorbonBiscuits
from assignment3.products.elaichi_biscuits import ElaichiBiscuits
from assignment3.products.wholegrain_biscuits import WholegrainBiscuits
from assignment3.products.multigrain_bread import MultigrainBread
from assignment3.products.pita_bread import PitaBread
from assignment3.products.whole_wheat_bread import WholeWheatBread


def get_product_class_from_name(name: str) -> type:
    return globals()[name]
