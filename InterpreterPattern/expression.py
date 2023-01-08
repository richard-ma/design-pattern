import abc


class Expression(abc.ABC):
    @abc.abstractmethod
    def interpreter(self, context: str):
        pass