import abc
from drawapi import DrawAPI


class Shape():
    def __init__(self, draw_api: "DrawAPI"):
        self._draw_api = draw_api

    @abc.abstractmethod
    def draw(self):
        pass