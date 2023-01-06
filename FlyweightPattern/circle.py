from shape import Shape


class Circle(Shape):
    def __init__(self, color: str):
        self._color = color
        self._x = None
        self._y = None
        self._radius = None

    def set_x(self, x: int):
        self._x = x

    def set_y(self, y: int):
        self._y = y

    def set_radius(self, radius: int):
        self._radius = radius 

    def draw(self):
        print(' '.join([
            "Circle: Draw() [ Color:",
            self._color,
            ", x:",
            str(self._x),
            ", y:",
            str(self._y),
            ", radius:",
            str(self._radius),
            "]"
        ]))


if __name__ == "__main__":
    shape = Circle("red")
    shape.set_x(33)
    shape.set_y(66)
    shape.set_radius(75)
    shape.draw()