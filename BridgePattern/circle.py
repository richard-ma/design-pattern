from shape import Shape
from drawapi import DrawAPI


class Circle(Shape):
    def __init__(self, x: int, y: int, radius: int, draw_api: "DrawAPI"):
        super().__init__(draw_api)
        self._x = x
        self._y = y
        self._radius = radius

    def draw(self):
        self._draw_api.draw_circle(self._radius, self._x, self._y)


if __name__ == "__main__":
    from greencircle import GreenCircle
    from redcircle import RedCircle
    
    shape = Circle(2, 3, 5, RedCircle())
    shape.draw()

    shape = Circle(1, 1, 3, GreenCircle())
    shape.draw()