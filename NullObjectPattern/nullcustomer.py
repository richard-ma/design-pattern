from abstractcustomer import AbstractCustomer


class NullCustomer(AbstractCustomer):
    def get_name(self):
        return "Not Available in Customer Database"

    def is_nil(self):
        return True


if __name__ == "__main__":
    customer = NullCustomer()

    print(customer.get_name())
    print(customer.is_nil())