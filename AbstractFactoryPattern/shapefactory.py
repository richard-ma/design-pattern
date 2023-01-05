from shape import Shape
from circle import Circle
from square import Square
from rectangle import Rectangle
from abstractfactory import AbstractFactory


class ShapeFactory(AbstractFactory):
    def get_color(self, color_type: str) -> "Color":
        pass

    def get_shape(self, shape_type: str) -> "Shape":
        if shape_type is None:
            raise TypeError("shape_type is not string: ", shape_type)

        shape_type = shape_type.lower()
        if (shape_type == 'circle'):
            return Circle()
        elif (shape_type == 'square'):
            return Square()
        elif (shape_type == 'rectangle'):
            return Rectangle()
        else:
            raise ValueError("shape_type not found: ", shape_type)


if __name__ == "__main__":
    shapeFactory = ShapeFactory()

    shape = shapeFactory.get_shape('circle')
    shape.draw()
    shape = shapeFactory.get_shape('square')
    shape.draw()
    shape = shapeFactory.get_shape('rectangle')
    shape.draw()