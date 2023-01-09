from customerfactory import CustomerFactory


if __name__ == "__main__":
    c1 = CustomerFactory.get_customer("Rob")
    c2 = CustomerFactory.get_customer("Bob")
    c3 = CustomerFactory.get_customer("Julie")
    c4 = CustomerFactory.get_customer("Laura")

    print("Customers:")
    print(c1.get_name())
    print(c2.get_name())
    print(c3.get_name())
    print(c4.get_name())