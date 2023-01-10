from client import Client


if __name__ == "__main__":
    c = Client()
    c.set_data("Test", "Data")
    c.print_data()
    c.set_data("Second Test", "Data2")
    c.print_data()