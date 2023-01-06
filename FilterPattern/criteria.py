import abc


class Criteria(abc.ABC):
    @abc.abstractmethod
    def meet_criteria(self, persons: list):
        pass