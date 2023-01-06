from circle import Circle


class ShapeFactory:
    circleMap = dict()
    
    @staticmethod
    def get_circle(color: str):
        circle = ShapeFactory.circleMap.get(color, None)

        if circle is None:
            circle = Circle(color)
            ShapeFactory.circleMap[color] = circle
            print("Creating circle of color:", color)

        return circle


if __name__ == "__main__":
    orig_red = ShapeFactory.get_circle("red")
    ShapeFactory.get_circle("green")
    new_red = ShapeFactory.get_circle("red")

    assert orig_red == new_red