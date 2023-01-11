from service import Service


class Service2(Service):
    def execute(self):
        print("Execting Service2")
    
    def get_name(self):
        return "Service2"