import abc


class Observer():
    def __init__(self):
        self._subject = None

    @abc.abstractmethod
    def update(self):
        pass