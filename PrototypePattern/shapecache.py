from shape import Shape
from circle import Circle
from square import Square
from rectangle import Rectangle


class ShapeCache():
    def __init__(self):
        self._shape_map = dict()

    def get_shape(self, shape_id: str):
        cached_shape = self._shape_map.get(shape_id)
        return cached_shape.clone()

    def load_cache(self):
        shape = Circle()
        shape.set_id("1")
        self._shape_map[shape.get_id()] = shape

        shape = Square()
        shape.set_id("2")
        self._shape_map[shape.get_id()] = shape

        shape = Rectangle()
        shape.set_id("3")
        self._shape_map[shape.get_id()] = shape


if __name__ == "__main__":
    sc = ShapeCache()
    sc.load_cache()

    clonedShape = sc.get_shape("1")
    print("Shape:", clonedShape.get_type()) 

    clonedShape = sc.get_shape("2")
    print("Shape:", clonedShape.get_type()) 

    clonedShape = sc.get_shape("3")
    print("Shape:", clonedShape.get_type()) 