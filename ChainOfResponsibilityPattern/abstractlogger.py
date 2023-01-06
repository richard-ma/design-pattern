import abc


class AbstractLogger:
    INFO = 1
    DEBUG = 2
    ERROR = 3

    def __init__(self):
        self._level = None
        self._nextLogger = None

    def set_next_logger(self, nextLogger: "AbstractLogger"):
        self._nextLogger = nextLogger

    def log_message(self, level: int, message: str):
        if self._level <= level:
            self.write(message)
        
        if self._nextLogger is not None:
            self._nextLogger.log_message(level, message)

    @abc.abstractmethod
    def write(self, message: str):
        pass