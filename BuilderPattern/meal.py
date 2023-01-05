from item import Item


class Meal:
    def __init__(self):
        self._items = list()

    def add(self, item: "Item") -> None:
        self._items.append(item)

    def get_cost(self):
        cost = 0
        for item in self._items:
            cost += item.price()
        return cost

    def show(self):
        for item in self._items:
            print("Item: ", item.name(), end=' ')
            print("Packing: ", item.packing().pack(), end=' ')
            print("Price: ", item.price())