from dependentobject1 import DependentObject1
from dependentobject2 import DependentObject2


class CoarseGrainedObject:
    def __init__(self):
        self._do1 = DependentObject1()
        self._do2 = DependentObject2()

    def set_data(self, data1: str, data2: str):
        self._do1.set_data(data1)
        self._do2.set_data(data2)

    def get_data(self):
        return [self._do1.get_data(), self._do2.get_data()]