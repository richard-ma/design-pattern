import abc


class Container(abc.ABC):
    @abc.abstractmethod
    def get_iterator(self):
        pass