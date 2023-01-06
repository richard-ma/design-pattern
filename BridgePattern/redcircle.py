from drawapi import DrawAPI


class RedCircle(DrawAPI):
    def draw_circle(self, radius: int, x: int, y: int):
        print("Drawing Circle[ color: red, radius:", radius, ", x:", x, ", y:", y, "]")


if __name__ == "__main__":
    api = RedCircle()
    api.draw_circle(3, 1, 1)