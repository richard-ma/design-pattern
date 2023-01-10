from compositeentity import CompositeEntity


class Client:
    def __init__(self):
        self._composite_entity = CompositeEntity()

    def print_data(self):
        for data in self._composite_entity.get_data():
            print("Data:", data)

    def set_data(self, data1: str, data2: str):
        self._composite_entity.set_data(data1, data2)