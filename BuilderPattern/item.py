import abc


class Item(abc.ABC): # this is an INTERFACE
    @abc.abstractmethod
    def name(self):
        pass

    @abc.abstractmethod
    def packing(self):
        pass

    @abc.abstractmethod
    def price(self):
        pass