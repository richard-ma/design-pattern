from shape import Shape


class Rectangle(Shape):
    def draw(self):
        print("Rectangle::draw()")


if __name__ == "__main__":
    shape = Rectangle()
    shape.draw()
