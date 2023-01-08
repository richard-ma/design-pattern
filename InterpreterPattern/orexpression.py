from expression import Expression


class OrExpression(Exception):
    def __init__(self, expr1: "Expression", expr2: "Expression"):
        self._expr1 = expr1
        self._expr2 = expr2

    def interpreter(self, context: str):
        return self._expr1.interpreter(context) or self._expr2.interpreter(context)


if __name__ == "__main__":
    from terminalexpression import TerminalExpression
    expr1 = TerminalExpression("ab")
    expr2 = TerminalExpression("ef")
    expr = OrExpression(expr1, expr2)
    print(expr.interpreter("abcd"))
    print(expr.interpreter("efgh"))
    print(expr.interpreter("jj"))