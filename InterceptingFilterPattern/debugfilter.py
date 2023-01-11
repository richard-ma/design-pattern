from filter import Filter


class DebugFilter(Filter):
    def execute(self, request: str):
        print("Request log:", request)