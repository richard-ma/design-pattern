import abc


class Strategy(abc.ABC):
    @abc.abstractmethod
    def do_operation(self, num1: int, num2: int):
        pass