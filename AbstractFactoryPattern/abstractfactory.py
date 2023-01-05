import abc


class AbstractFactory(abc.ABC):
    @abc.abstractmethod
    def get_color(self, color_type: str) -> "Color":
        pass

    @abc.abstractmethod
    def get_shape(self, shape_type: str) -> "Shape":
        pass