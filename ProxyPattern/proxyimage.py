from image import Image
from realimage import RealImage


class ProxyImage(Image):
    def __init__(self, filename: str):
        self._filename = filename
        self._realImage = None

    def display(self):
        if self._realImage is None:
            self._realImage = RealImage(self._filename)
        self._realImage.display()


if __name__ == "__main__":
    image = ProxyImage("test_10mb.jpg")
    image.display()
    image.display()