class Memento:
    def __init__(self, state: str):
        self._state = state

    def get_state(self):
        return self._state


if __name__ == "__main__":
    m = Memento("hello")
    print(m.get_state())