from terminalexpression import TerminalExpression
from orexpression import OrExpression
from andexpression import AndExpression


if __name__ == "__main__":
    robert = TerminalExpression("Robert")
    john = TerminalExpression("John")
    is_male = OrExpression(robert, john)

    julie = TerminalExpression("Julie")
    married = TerminalExpression("Married")
    is_married_woman = AndExpression(julie, married)

    print("John is male?", is_male.interpreter("John"))
    print("Julie is a married women?", is_married_woman.interpreter("Married Julie"))