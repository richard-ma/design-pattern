from item import Item
from wrapper import Wrapper


class Burger(Item):
    def packing(self):
        return Wrapper()

    def name(self):
        pass

    def price(self):
        pass


if __name__ == "__main__":
    burger = Burger()
    print(burger.packing())
    burger.name()
    burger.price()