import abc


class Color(abc.ABC):
    @abc.abstractmethod
    def fill(self):
        pass