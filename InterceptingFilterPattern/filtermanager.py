from filterchain import FilterChain
from target import Target


class FilterManager:
    def __init__(self, target: "Target"):
        self._filter_chain = FilterChain()
        self._filter_chain.set_target(target)

    def set_filter(self, filter: "Filter"):
        self._filter_chain.add_filter(filter)

    def filter_request(self, request: str):
        self._filter_chain.execute(request)