from shape import Shape


class Rectangle(Shape):
    def __init__(self):
        self._type = "Rectangle"

    def draw(self):
        print("Rectangle::draw()")


if __name__ == "__main__":
    shape = Rectangle()
    shape.draw()
