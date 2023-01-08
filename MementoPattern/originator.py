from memento import Memento


class Originator:
    def __init__(self):
        self._state = None

    def set_state(self, state: str):
        self._state = state

    def get_state(self):
        return self._state
    
    def save_state_to_memento(self):
        return Memento(self._state)

    def get_state_from_memento(self, memento: "Memento"):
        self._state = memento.get_state()


if __name__ == "__main__":
    o = Originator()
    o.set_state("UPDATE")
    print(o.get_state())
    m = o.save_state_to_memento()
    o.get_state_from_memento(m)
    print(o.get_state())