import abc


class Service(abc.ABC):
    @abc.abstractmethod
    def get_name(self):
        pass

    @abc.abstractmethod
    def execute(self):
        pass