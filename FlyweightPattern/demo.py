from circle import Circle
from shapefactory import ShapeFactory
import random


if __name__ == "__main__":
    def get_random_color(colors: list):
        return random.choice(colors)

    def get_random_x():
        return random.randint(0, 100)

    def get_random_y():
        return random.randint(0, 100)

    colors = ['red', 'green', 'blue', 'white', 'black']

    for i in range(20):
        circle = ShapeFactory.get_circle(get_random_color(colors))
        circle.set_x(get_random_x())
        circle.set_y(get_random_y())
        circle.set_radius(100)
        circle.draw()