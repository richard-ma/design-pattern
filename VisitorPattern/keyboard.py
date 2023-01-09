from computerpart import ComputerPart


class Keyboard(ComputerPart):
    def accept(self, computer_part_visitor: "ComputerPartVisitor"):
        computer_part_visitor.visit(self)