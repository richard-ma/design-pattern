import abc


class BusinessService(abc.ABC):
    @abc.abstractmethod
    def do_processing(self):
        pass