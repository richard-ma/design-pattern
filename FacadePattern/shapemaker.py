from circle import Circle
from rectangle import Rectangle
from square import Square


class ShapeMaker:
    def __init__(self):
        self._circle = Circle()
        self._rectangle = Rectangle()
        self._square = Square()

    def draw_circle(self):
        self._circle.draw()

    def draw_rectangle(self):
        self._rectangle.draw()

    def draw_square(self):
        self._square.draw()


if __name__ == "__main__":
    sm = ShapeMaker()

    sm.draw_circle()
    sm.draw_rectangle()
    sm.draw_square()