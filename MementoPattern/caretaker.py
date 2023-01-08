from memento import Memento


class CareTaker:
    def __init__(self):
        self._memento_list = list()

    def add(self, state: Memento):
        self._memento_list.append(state)

    def get(self, index: int):
        return self._memento_list[index]