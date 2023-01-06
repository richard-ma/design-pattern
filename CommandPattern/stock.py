class Stock:
    def __init__(self):
        self._name = "ABC"
        self._quantity = 10

    def buy(self):
        print(' '.join([
            "Stock [ Name:",
            self._name,
            ", Quantity:",
            str(self._quantity),
            "] bought"
        ]))

    def sell(self):
        print(' '.join([
            "Stock [ Name:",
            self._name,
            ", Quantity:",
            str(self._quantity),
            "] sold"
        ]))


if __name__ == "__main__":
    s = Stock()
    s.buy()
    s.sell()