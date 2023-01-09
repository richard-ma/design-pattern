import abc


class AbstractCustomer():
    def __init__(self):
        self._name = ""

    @abc.abstractmethod
    def is_nil(self):
        pass

    @abc.abstractmethod
    def get_name(self):
        pass