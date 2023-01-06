from stock import Stock
from order import Order


class SellStock(Order):
    def __init__(self, s: "Stock"):
        self._abc_stock = s

    def execute(self):
        self._abc_stock.sell()


if __name__ == "__main__":
    s = Stock()
    order = SellStock(s)
    order.execute()