from service import Service


class Service1(Service):
    def execute(self):
        print("Execting Service1")
    
    def get_name(self):
        return "Service1"