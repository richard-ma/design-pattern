class Context:
    def __init__(self):
        self._state = None

    def set_state(self,  state: "State"):
        self._state = state

    def get_state(self):
        return self._state