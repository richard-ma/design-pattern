class Context:
    def __init__(self, strategy: "Strategy"):
        self._strategy = strategy

    def execute_strategy(self, num1: int, num2: int):
        return self._strategy.do_operation(num1, num2)