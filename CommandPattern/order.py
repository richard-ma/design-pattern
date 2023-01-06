import abc


class Order(abc.ABC):
    @abc.abstractmethod
    def execute(self):
        pass