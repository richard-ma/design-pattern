from businessdelegate import BusinessDelegate
from client import Client


if __name__ == "__main__":
    bd = BusinessDelegate()
    bd.set_service_type("ejb")

    c = Client(bd)
    c.do_task()

    bd.set_service_type("jms")
    c.do_task()

    bd.set_service_type("other")
    c.do_task()