import abc


class Filter:
    @abc.abstractmethod
    def execute(self, request: str):
        pass