from shape import Shape


class Square(Shape):
    def __init__(self):
        self._type = "Square"

    def draw(self):
        print("Square::draw()")


if __name__ == "__main__":
    shape = Square()
    shape.draw()