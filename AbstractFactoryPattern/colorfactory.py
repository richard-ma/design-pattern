from color import Color
from red import Red
from green import Green
from blue import Blue
from abstractfactory import AbstractFactory


class ColorFactory(AbstractFactory):
    def get_shape(self, shape_type: str) -> "Shape":
        pass

    def get_color(self, color_type: str) -> "Color":
        if color_type is None:
            raise TypeError("color_type is not string: ", color_type)

        color_type = color_type.lower()
        if (color_type == 'red'):
            return Red()
        elif (color_type == 'green'):
            return Green()
        elif (color_type == 'blue'):
            return Blue()
        else:
            raise ValueError("color_type not found: ", color_type)


if __name__ == "__main__":
    colorFactory = ColorFactory()

    color = colorFactory.get_color('red')
    color.fill()
    color = colorFactory.get_color('green')
    color.fill()
    color = colorFactory.get_color('blue')
    color.fill()