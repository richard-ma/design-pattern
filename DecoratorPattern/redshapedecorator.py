from shape import Shape
from shapedecorator import ShapeDecorator


class RedShapeDecorator(ShapeDecorator):
    def __init__(self, decorated_shape: "Shape"):
        super().__init__(decorated_shape)

    def draw(self):
        self._decorated_shape.draw()
        self.set_red_border(self._decorated_shape)

    def set_red_border(self, decorated_shape: "Shape"):
        print("Border Color: Red")

    
if __name__ == "__main__":
    from circle import Circle
    from rectangle import Rectangle

    circle = Circle()
    redCircle = RedShapeDecorator(Circle())
    redRectangle = RedShapeDecorator(Rectangle())

    print("Circle with normal border.")
    circle.draw()

    print("Circle with red border")
    redCircle.draw()

    print("Rectangle with red border")
    redRectangle.draw()