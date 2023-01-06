from stock import Stock
from order import Order


class BuyStock(Order):
    def __init__(self, s: "Stock"):
        self._abc_stock = s

    def execute(self):
        self._abc_stock.buy()


if __name__ == "__main__":
    s = Stock()
    order = BuyStock(s)
    order.execute()