import abc


class Image(abc.ABC):
    @abc.abstractmethod
    def display(self):
        pass