from strategy import Strategy


class OperationSubtract(Strategy):
    def do_operation(self, num1: int, num2: int):
        return num1 - num2


if __name__ == "__main__":
    num1 = 3
    num2 = 2
    s = OperationSubtract()
    print(s.do_operation(num1, num2))