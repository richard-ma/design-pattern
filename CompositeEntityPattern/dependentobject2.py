class DependentObject2:
    def __init__(self):
        self._data = None

    def set_data(self, data: str):
        self._data = data

    def get_data(self):
        return self._data


if __name__ == "__main__":
    obj = DependentObject2()
    obj.set_data("data")
    print(obj.get_data())