from item import Item
from bottle import Bottle


class ColdDrink(Item):
    def packing(self):
        return Bottle()

    def name(self):
        pass

    def price(self):
        pass


if __name__ == "__main__":
    cold_drink = ColdDrink()

    print(cold_drink.packing())
    cold_drink.name()
    cold_drink.price()