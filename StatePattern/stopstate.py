from state import State


class StopState(State):
    def do_action(self, context: "Context"):
        print("Player is in stop state.")
        context.set_state(self)

    def __str__(self):
        return "Stop State"