from businesslookup import BusinessLookUp


class BusinessDelegate:
    def __init__(self):
        self._lookup_service = BusinessLookUp()
        self._business_service = None
        self._service_type = None

    def set_service_type(self, service_type: str):
        self._service_type = service_type

    def do_task(self):
        self._business_service = self._lookup_service.get_business_service(self._service_type)
        self._business_service.do_processing()


if __name__ == "__main__":
    bd = BusinessDelegate()
    bd.set_service_type('ejb')
    bd.do_task()
    bd.set_service_type('jms')
    bd.do_task()
    bd.set_service_type('other')
    bd.do_task()