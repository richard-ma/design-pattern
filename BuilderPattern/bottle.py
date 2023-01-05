from packing import Packing


class Bottle(Packing):
    def pack(self):
        return "Bottle"


if __name__ == "__main__":
    bottle = Bottle()
    print(bottle.pack())