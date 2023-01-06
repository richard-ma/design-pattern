from image import Image


class RealImage(Image):
    def __init__(self, filename: str):
        self._filename = filename
        self._load_from_disk(filename)

    def display(self):
        print("Displaying", self._filename)

    def _load_from_disk(self, filename: str):
        print("Loading", filename)


if __name__ == "__main__":
    image = RealImage("realimage")
    image.display()
    image.display()