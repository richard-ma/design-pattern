from dispatcher import Dispatcher


class FrontController:
    def __init__(self):
        self._dispatcher = Dispatcher()

    def is_authentic_user(self):
        print("User is authenticated successfully.")
        return True

    def track_request(self, request: str):
        print("Page requested:", request)

    def dispatch_request(self, request: str):
        self.track_request(request)
        if self.is_authentic_user():
            self._dispatcher.dispatch(request)