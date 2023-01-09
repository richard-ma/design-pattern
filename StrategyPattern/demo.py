from operationadd import OperationAdd
from operationsubtract import OperationSubtract
from operationmultiply import OperationMultiply
from context import Context


if __name__ == "__main__":
    context = Context(OperationAdd())
    print("10 + 5 =", context.execute_strategy(10, 5))
    context = Context(OperationSubtract())
    print("10 - 5 =", context.execute_strategy(10, 5))
    context = Context(OperationMultiply())
    print("10 * 5 =", context.execute_strategy(10, 5))