import abc


class Shape(abc.ABC):
    @abc.abstractmethod
    def draw(self) -> None:
        pass