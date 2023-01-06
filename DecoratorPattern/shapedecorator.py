from shape import Shape


class ShapeDecorator(Shape):
    def __init__(self, decorated_shape: "Shape"):
        self._decorated_shape = decorated_shape

    def draw(self):
        self._decorated_shape.draw()