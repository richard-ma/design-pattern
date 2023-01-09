import abc


class ComputerPartVisitor(abc.ABC):
    @abc.abstractmethod
    def visit(self, obj: "ComputerPart"):
        pass