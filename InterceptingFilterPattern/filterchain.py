from filter import Filter
from target import Target


class FilterChain:
    def __init__(self):
        self._filters = list()
        self._target = Target()

    def add_filter(self, filter: "Filter"):
        self._filters.append(filter)

    def execute(self, request: str):
        for filter in self._filters:
            filter.execute(request)
        self._target.execute(request)

    def set_target(self, target: "Target"):
        self._target = target