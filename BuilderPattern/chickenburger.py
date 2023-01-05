from burger import Burger


class ChickenBurger(Burger):
    def price(self):
        return 50.5

    def name(self):
        return "Chicken Burger"


if __name__ == "__main__":
    cb = ChickenBurger()

    print(cb.price())
    print(cb.name())