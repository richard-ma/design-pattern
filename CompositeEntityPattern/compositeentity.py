from coarsegrainedobject import CoarseGrainedObject


class CompositeEntity:
    def __init__(self):
        self._cgo = CoarseGrainedObject()

    def set_data(self, data1: str, data2: str):
        self._cgo.set_data(data1, data2)

    def get_data(self):
        return self._cgo.get_data()