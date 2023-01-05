import abc


class Packing(abc.ABC): # this is an INTERFACE
    @abc.abstractmethod
    def pack(self):
        pass