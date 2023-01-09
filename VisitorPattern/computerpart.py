import abc


class ComputerPart(abc.ABC):
    @abc.abstractmethod
    def accept(self, computer_part_visitor: "ComputerPartVisitor"):
        pass