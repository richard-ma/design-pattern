import inspect
from color import Color


def get__function_name():
    return inspect.stack()[1][3]

class Green(Color):
    def fill(self):
        print(self.__class__.__name__ + "::" + get__function_name() + "()")


if __name__ == "__main__":
    color = Green()
    color.fill()