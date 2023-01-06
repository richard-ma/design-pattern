import abc


class DrawAPI(abc.ABC):
    @abc.abstractmethod
    def draw_circle(self, radius: int, x: int, y: int):
        pass