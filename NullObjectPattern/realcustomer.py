from abstractcustomer import AbstractCustomer


class RealCustomer(AbstractCustomer):
    def __init__(self, name: str):
        self._name = name

    def get_name(self):
        return self._name

    def is_nil(self):
        return False


if __name__ == "__main__":
    customer = RealCustomer("name")
    print(customer.get_name())
    print(customer.is_nil())