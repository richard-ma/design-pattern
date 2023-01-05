import copy
import abc


class Shape(abc.ABC):
    def __init__(self):
        self._id = None
        self._type = None

    def get_type(self):
        return self._type

    def get_id(self):
        return self._id

    def set_id(self, id: str):
        self._id = id

    @abc.abstractmethod
    def draw(self) -> None:
        pass

    def clone(self):
        return copy.deepcopy(self)