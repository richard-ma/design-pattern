from expression import Expression


class TerminalExpression(Exception):
    def __init__(self, data: str):
        self._data = data

    def interpreter(self, context: str):
        if self._data in context:
            return True
        return False


if __name__ == "__main__":
    expr = TerminalExpression('da')
    print(expr.interpreter('data'))
    print(expr.interpreter('te'))