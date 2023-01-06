from order import Order


class Broker:
    def __init__(self):
        self._order_list = list()

    def take_order(self, order: "Order"):
        self._order_list.append(order)

    def place_orders(self):
        for order in self._order_list:
            order.execute()
        self._order_list = list() # clear order list


if __name__ == "__main__":
    from stock import Stock
    from buystock import BuyStock
    from sellstock import SellStock

    abcStock = Stock()

    buyStockOrder = BuyStock(abcStock)
    sellStockOrder = SellStock(abcStock)

    broker = Broker()
    broker.take_order(buyStockOrder)
    broker.take_order(sellStockOrder)

    broker.place_orders()