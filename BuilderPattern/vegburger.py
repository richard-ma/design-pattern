from burger import Burger


class VegBurger(Burger):
    def price(self):
        return 25.0
    
    def name(self):
        return "Veg Burger"


if __name__ == "__main__":
    vb = VegBurger()

    print(vb.price())
    print(vb.name())