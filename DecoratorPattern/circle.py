from shape import Shape


class Circle(Shape):
    def draw(self):
        print("Circle::draw()")


if __name__ == "__main__":
    shape = Circle()
    shape.draw()