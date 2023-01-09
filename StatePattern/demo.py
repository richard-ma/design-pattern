from context import Context
from startstate import StartState
from stopstate import StopState


if __name__ == "__main__":
    context = Context()

    startState = StartState()
    startState.do_action(context)

    print(context.get_state())

    stopState = StopState()
    stopState.do_action(context)

    print(context.get_state())