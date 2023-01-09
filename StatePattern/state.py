import abc


class State(abc.ABC):
    @abc.abstractmethod
    def do_action(self, context: "Context"):
        pass