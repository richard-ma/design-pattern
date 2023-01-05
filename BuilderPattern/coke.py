from colddrink import ColdDrink


class Coke(ColdDrink):
    def price(self):
        return 30.0

    def name(self):
        return "Coke"


if __name__ == "__main__":
    coke = Coke()

    print(coke.price())
    print(coke.name())