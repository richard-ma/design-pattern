from realcustomer import RealCustomer
from nullcustomer import NullCustomer


class CustomerFactory:
    NAMES = ["Rob", "Joe", "Julie"]

    @staticmethod
    def get_customer(name: str):
        if name in CustomerFactory.NAMES:
            return RealCustomer(name)
        else:
            return NullCustomer()


if __name__ == "__main__":
    realCustomer = CustomerFactory.get_customer("Joe")
    nullCustomer = CustomerFactory.get_customer("test")

    print(realCustomer.is_nil())
    print(nullCustomer.is_nil())