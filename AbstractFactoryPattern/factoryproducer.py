from shapefactory import ShapeFactory
from colorfactory import ColorFactory


class FactoryProducer():
    @staticmethod
    def get_factory(factory_type: str) -> "AbstractFactory":
        factory_type = factory_type.lower()

        if factory_type == "shape":
            return ShapeFactory()
        elif factory_type == "color":
            return ColorFactory()
        else:
            raise ValueError("factory_type not found: ", factory_type)


if __name__ == "__main__":
    sf = FactoryProducer.get_factory('shape')
    shape = sf.get_shape('circle')
    shape.draw()
    shape = sf.get_shape('rectangle')
    shape.draw()
    shape = sf.get_shape('circle')
    shape.draw()
    cf = FactoryProducer.get_factory('color')
    color = cf.get_color('red')
    color.fill()
    color = cf.get_color('green')
    color.fill()
    color = cf.get_color('blue')
    color.fill()