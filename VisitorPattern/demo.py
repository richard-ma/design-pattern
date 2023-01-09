from computer import Computer
from computerpartdisplayvisitor import ComputerPartDisplayVisitor


if __name__ == "__main__":
    computer = Computer()
    computer.accept(ComputerPartDisplayVisitor())