from shape import Shape


class Circle(Shape):
    def __init__(self):
        self._type = "Circle"

    def draw(self):
        print("Circle::draw()")


if __name__ == "__main__":
    shape = Circle()
    shape.draw()