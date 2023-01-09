from computerpart import ComputerPart
from mouse import Mouse
from keyboard import Keyboard
from monitor import Monitor


class Computer(ComputerPart):
    def __init__(self):
        self._parts = list()
        self._parts += [Mouse(), Keyboard(), Monitor()]


    def accept(self, computer_part_visitor: "ComputerPartVisitor"):
        for part in self._parts:
            part.accept(computer_part_visitor)

        computer_part_visitor.visit(self)