from service1 import Service1
from service2 import Service2


class InitialContext:
    def lookup(self, jndi_name: str):
        if jndi_name.lower() == "SERVICE1".lower():
            print("Looking up and creating a new service1 object")
            return Service1()
        elif jndi_name.lower() == "SERVICE2".lower():
            print("Looking up and creating a new service2 object")
            return Service2()

        return None