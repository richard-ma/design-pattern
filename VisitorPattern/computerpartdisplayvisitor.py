from computerpartvisitor import ComputerPartVisitor
from computer import Computer
from mouse import Mouse
from keyboard import Keyboard
from monitor import Monitor


class ComputerPartDisplayVisitor(ComputerPartVisitor):
    def visit(self, object: "ComputerPart"):
        if isinstance(object, Computer):
            print("Displaying Computer")
        elif isinstance(object, Mouse):
            print("Displaying Mouse")
        elif isinstance(object, Keyboard):
            print("Displaying Keyboard")
        elif isinstance(object, Monitor):
            print("Displaying Monitor")
        else:
            raise TypeError(object.__class__.__name__ + "is not supported.")