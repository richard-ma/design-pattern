from filter import Filter


class AuthenticationFilter(Filter):
    def execute(self, request: str):
        print("Authentication request:", request)