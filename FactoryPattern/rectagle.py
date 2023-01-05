from shape import Shape


class Rectagle(Shape):
    def draw(self):
        print("Rectagle::draw()")


if __name__ == "__main__":
    shape = Rectagle()
    shape.draw()
