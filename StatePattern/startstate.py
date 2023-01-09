from state import State


class StartState(State):
    def do_action(self, context: "Context"):
        print("Player is in start state.")
        context.set_state(self)

    def __str__(self):
        return "Start State"