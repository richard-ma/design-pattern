from servicelocator import ServiceLocator


if __name__ == "__main__":
    service = ServiceLocator.get_service("Service1")
    service.execute()
    service = ServiceLocator.get_service("Service2")
    service.execute()
    service = ServiceLocator.get_service("Service1")
    service.execute()
    service = ServiceLocator.get_service("Service2")
    service.execute()