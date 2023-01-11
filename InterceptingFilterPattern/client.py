from filtermanager import FilterManager


class Client:
    def __init__(self):
        self._filter_manager = None

    def set_fitler_manager(self, fitler_manager: "FilterManager"):
        self._filter_manager = fitler_manager

    def send_request(self, request: str):
        self._filter_manager.filter_request(request)