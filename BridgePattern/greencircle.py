from drawapi import DrawAPI


class GreenCircle(DrawAPI):
    def draw_circle(self, radius: int, x: int, y: int):
        print("Drawing Circle[ color: green, radius:", radius, ", x:", x, ", y:", y, "]")


if __name__ == "__main__":
    api = GreenCircle()
    api.draw_circle(3, 1, 1)