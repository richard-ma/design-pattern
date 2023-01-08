from expression import Expression


class AndExpression(Expression):
    def __init__(self, expr1: "Expression", expr2: "Expression"):
        self._expr1 = expr1
        self._expr2 = expr2

    def interpreter(self, context: str):
        return self._expr1.interpreter(context) and self._expr2.interpreter(context)


if __name__ == "__main__":
    from terminalexpression import TerminalExpression

    expr1 = TerminalExpression("ab")
    expr2 = TerminalExpression("cd")
    expr = AndExpression(expr1, expr2)
    print(expr.interpreter("abff"))
    print(expr.interpreter("abcd"))
    print(expr.interpreter("ffcd"))