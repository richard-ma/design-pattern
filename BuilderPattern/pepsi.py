from colddrink import ColdDrink


class Pepsi(ColdDrink):
    def price(self):
        return 35.0

    def name(self):
        return "Pepsi"


if __name__ == "__main__":
    pepsi = Pepsi()

    print(pepsi.price())
    print(pepsi.name())