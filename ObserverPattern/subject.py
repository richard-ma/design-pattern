class Subject:
    def __init__(self):
        self._observers = list()
        self._state = 0

    def get_state(self):
        return self._state

    def set_state(self, state: int):
        self._state = state
        self.notify_all_observers()

    def attach(self, observer: "Observer"):
        self._observers.append(observer)

    def notify_all_observers(self):
        for observer in self._observers:
            observer.update()