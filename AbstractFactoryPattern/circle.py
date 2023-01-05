import inspect
from shape import Shape


def get__function_name():
    return inspect.stack()[1][3]

class Circle(Shape):
    def draw(self):
        print(self.__class__.__name__ + "::" + get__function_name() + "()")


if __name__ == "__main__":
    shape = Circle()
    shape.draw()