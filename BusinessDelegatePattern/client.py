from businessdelegate import BusinessDelegate


class Client:
    def __init__(self, business_service: "BusinessDelegate"):
        self._business_service = business_service

    def do_task(self):
        self._business_service.do_task()