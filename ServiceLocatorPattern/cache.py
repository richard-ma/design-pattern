class Cache:
    def __init__(self):
        self._services = list()
    
    def get_service(self, service_name: str):
        for service in self._services:
            if service.get_name().lower() == service_name.lower():
                print("Returning cached", service_name, "object")
                return service
        
        return None

    def add_service(self, new_service: "Service"):
        exists = False

        for service in self._services:
            if service.get_name().lower() == new_service.get_name().lower():
                exists = True
        
        if exists is None:
            self._services.append(new_service)